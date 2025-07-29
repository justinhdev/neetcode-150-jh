"""
Title: Valid Anagram - 242
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/
Language: Python3

Complexity:
Time - O(n) - iterates through each string once
Space - O(1) - number of unique lowercase letters is constant: 26 in each hash map

Content: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
• 1 <= s.length, t.length <= 5 * 10^4
• s and t consist of lowercase English letters.
• Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: if lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Initialize hash map for both strings
        s_map = {}
        t_map = {}

        # Count each character in string s
        for letter in s:
            s_map[letter] = s_map.get(letter, 0) + 1

        # Count each character in string t
        for letter in t:
            t_map[letter] = t_map.get(letter, 0) + 1

        # Compare both hash maps
        return s_map == t_map


from collections import Counter


# Solution using built-ins
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
