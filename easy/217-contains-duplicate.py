"""
Title: Contains Duplicate - 217
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/
Language: Python3

Complexity:
Time - O(n) - iterates once through the list, set operations are O(1) on average
Space - O(n) - in the worst case, all elements are added to the set

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

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to keep track of unique elements
        duplicatesSet = set()
        # Iterate through each number in the input list
        for n in nums:
            # If the number is already in the set, a duplicate exists
            if n in duplicatesSet:
                return True
            # Otherwise, add the number to the set
            duplicatesSet.add(n)
        # No duplicates found in the list
        return False
