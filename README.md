# 🧠 NeetCode 150 Solutions – Python

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/LeetCode-150%20Problems-orange)

This repository contains my Python solutions to the NeetCode 150 problems on LeetCode.

Each solution includes:

- Clean and optimized Python 3 code
- Auto-generated metadata headers with:
  - Problem title, difficulty, and link
  - Time and space complexity placeholders
  - Full problem description (Metadata fetched via LeetCode’s unofficial GraphQL API)
- Automatic sorting into `easy/`, `medium/`, or `hard/` directories

---

## 🔧 Tooling & Workflow

Problems are initially scaffolded using the **[LeetCode extension for VS Code](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode)**, which provides:

- Ability to browse, open, and solve LeetCode problems directly within VS Code

To streamline documentation and organization, this repo uses a custom Python script (`sort_problems.py`) to:

- Fetch problem metadata using the LeetCode GraphQL API
- Clean up formatting and remove boilerplate
- Inject standardized docstring headers with metadata and complexity sections
- Automatically move problems into difficulty-specific folders

This workflow helps keep problems clean, searchable, and easy to maintain — without automating the actual problem solving.

---

## Repository Structure

```
neetcode-150-jh/
├── easy/
│   ├── ###-problem-name.py
│   └── ...
├── medium/
│   └── ...
├── hard/
│   └── ...
├── sort_problems.py
├── requirements.txt
└── README.md
```

---

## Script: `sort_problems.py`

This script automates the organization and formatting of problem files by:

- Fetching problem metadata from LeetCode via their (unofficial) GraphQL API
- Cleaning and injecting standardized docstrings with problem details
- Renaming files to the format: `###-problem-title.py` (e.g., `217-contains-duplicate.py`)
- Sorting each file into its corresponding difficulty folder (`easy/`, `medium/`, `hard/`)

### Example Header (Auto-injected)

```python
"""
Title: Contains Duplicate - 217
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/
Language: Python3

Complexity:
Time - O()
Space - O()

Content: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
• 1 <= nums.length <= 10^5
• -10^9 <= nums[i] <= 10^9
"""
```

---

## Usage

1. **Install dependencies**  
   (create a virtual environment first if desired)

   ```bash
   pip install -r requirements.txt
   ```

2. **Place `.py` problem files** in the root of the repo(automatically done with LeetCode extension for VS Code)

3. **Run the sorter**
   ```bash
   python sort_problems.py
   ```

---

## Requirements

- Python 3.10+
- Dependencies from `requirements.txt`:
  - `requests`
  - `beautifulsoup4`

---

## Goals

This repo serves as:

- A polished portfolio of my LeetCode practice
- A framework to scale with future LeetCode topic lists
- A tool to keep solutions clean, standardized, and documented

---

## If you find this helpful...

Feel free to fork this repo or leave a ⭐️ — happy coding!
