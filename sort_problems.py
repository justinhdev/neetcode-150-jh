import os
import shutil
import requests
import re
from bs4 import BeautifulSoup, NavigableString


def extract_text_with_sup_in_code(html: str) -> str:
    """
    Parses LeetCode HTML content and cleans formatting:
    - Converts <sup> inside <code> tags to ^n (e.g., 10^9)
    - Replaces non-breaking spaces
    - Removes extra newlines after Example headers
    - Bullets each constraint line
    """
    soup = BeautifulSoup(html, "html.parser")

    # Replace <sup> inside <code> with ^number notation
    for code in soup.find_all("code"):
        if code.find("sup"):
            new_code = ""
            for child in code.children:
                if isinstance(child, NavigableString):
                    new_code += str(child)
                elif child.name == "sup":
                    new_code += "^" + child.get_text()
                else:
                    new_code += child.get_text()
            code.string = new_code

    # Replace non-breaking space characters
    raw_text = soup.get_text().replace("\u00a0", " ")

    # Remove blank lines directly after 'Example X:' lines
    raw_text = re.sub(r"(Example \d+:)\n\s*\n", r"\1\n", raw_text)

    # Format 'Constraints' section with bullets
    lines = raw_text.splitlines()
    output_lines = []
    in_constraints = False
    last_line_blank = False

    for line in lines:
        stripped = line.strip()

        if stripped == "Constraints:":
            if output_lines and output_lines[-1] != "":
                output_lines.append("")
            output_lines.append("Constraints:")
            in_constraints = True
            continue

        if in_constraints and stripped:
            output_lines.append(f"• {stripped}")
        elif not in_constraints:
            if stripped == "":
                if not last_line_blank:
                    output_lines.append("")
                    last_line_blank = True
            else:
                output_lines.append(line)
                last_line_blank = False

    return "\n".join(output_lines).strip()


def normalize_slug(filename: str) -> str:
    """
    Converts a filename to its LeetCode slug format.
    Example: '217.ContainsDuplicate.py' -> 'contains-duplicate'
    """
    base = filename.rsplit(".", 1)[0]
    base = re.sub(r"^\d+\.", "", base)
    base = re.sub(r"[_\s]+", "-", base)
    base = re.sub(r"(?<=[a-z0-9])([A-Z])", r"-\1", base)
    return base.lower()


def get_problem_details(slug: str) -> dict[str, str] | None:
    """
    Queries the LeetCode GraphQL API to fetch metadata for the given slug.
    Returns a dictionary with id, title, difficulty, and content.
    """
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
    }
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
          }
        }
        """,
        "variables": {"titleSlug": slug},
    }

    res = requests.post(url, json=query, headers=headers)
    if not res.ok:
        return None

    data = res.json().get("data", {}).get("question", None)
    if not data:
        return None

    content_text = extract_text_with_sup_in_code(data["content"])

    return {
        "id": data["questionFrontendId"],
        "title": data["title"],
        "difficulty": data["difficulty"],
        "content": content_text.strip(),
    }


def is_generated_header_line(line: str) -> bool:
    """
    Identifies old header/comment lines to strip before injecting a new header.
    """
    stripped = line.strip()
    return (
        stripped.startswith("# @lc")
        or stripped == "#"
        or re.match(r"#\s*\[\d+\]", stripped)
        or re.match(r"#\s*\[\d+\]\s+.+", stripped)
    )


def inject_header(filepath: str, details: dict[str, str], slug: str) -> None:
    """
    Adds a formatted metadata docstring to the top of a solution file.
    Skips injection if a header already exists.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove existing metadata/header lines
    cleaned_lines = [line for line in lines if not is_generated_header_line(line)]
    cleaned_code = "".join(cleaned_lines).lstrip()

    lines = cleaned_code.splitlines()
    if lines and "Title:" in lines[0]:
        return  # Already contains a header

    # Build docstring header block
    header = f'"""\nTitle: {details["title"]} - {details["id"]}\n'
    header += f'Difficulty: {details["difficulty"]}\n'
    header += f"Link: https://leetcode.com/problems/{slug}/\n"
    header += "Language: Python3\n\n"
    header += "Complexity:\n"
    header += "Time - O()\n"
    header += "Space - O()\n\n"
    header += f'Content: {details["content"]}\n'
    header += '"""\n\n\n'

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + cleaned_code)


def sort_solutions() -> None:
    """
    Main driver: scans current directory for .py solution files,
    fetches metadata, injects headers, and moves files by difficulty.
    """
    current_dir = os.getcwd()
    exclude = {"sort_solutions.py"}

    files = sorted(
        f
        for f in os.listdir(current_dir)
        if f.endswith(".py") and os.path.isfile(f) and f not in exclude
    )

    for filename in files:
        slug = normalize_slug(filename)
        details = get_problem_details(slug)

        if not details:
            print(f"⚠️ Could not fetch metadata for: {filename} (slug: {slug})")
            continue

        # Build new filename: "###-problem-name.py"
        new_filename = f"{details['id']}-{slug}.py"

        difficulty = details["difficulty"].lower()
        target_dir = os.path.join(current_dir, difficulty)
        os.makedirs(target_dir, exist_ok=True)

        source_path = os.path.join(current_dir, filename)
        dest_path = os.path.join(target_dir, new_filename)

        shutil.move(source_path, dest_path)
        inject_header(dest_path, details, slug)
        print(f"Moved and renamed {filename} → {difficulty}/{new_filename}")


if __name__ == "__main__":
    sort_solutions()
