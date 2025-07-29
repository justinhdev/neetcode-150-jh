"""
Title: Group Anagrams - 49
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
Language: Python3

Complexity:
Time - O(n * k) - Iterates through each (n) word and for each word, iterates through its (k) letters to build a 26-length frequency array.
Space - O(n * k) - Stores up to (n) unique frequency keys, and all (n) words with up to (k) characters each in grouped lists.

Content: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
• 1 <= strs.length <= 10^4
• 0 <= strs[i].length <= 100
• strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        words_map = {}  # key: stringified letter count, value: list of words

        for word in strs:
            # Manually count each character (26-length list)
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                count[index] += 1

            # Convert count list into a string key (e.g., "1,0,0,...")
            key = ""
            for num in count:
                key += str(num) + ","

            # Check if key exists in dictionary
            if key not in words_map:
                words_map[key] = []
            words_map[key].append(word)

        # Convert map values into list of lists
        result = []
        for group in words_map:
            result.append(words_map[group])

        return result


class SolutionBuiltIns:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        # Use a dictionary to group anagrams by their sorted key
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word to get the canonical form (e.g., 'eat' -> 'aet')
            key = "".join(sorted(word))

            # Group the original word under the sorted key
            anagram_map[key].append(word)

        # Return the grouped anagram lists
        return list(anagram_map.values())
