# Problem: Two Sum
# Link to LeetCode problem: https://leetcode.com/problems/two-sum/

# Description:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# ------------------------------------------------------------
# 🧠 Solution Approaches:
# 1) Brute Force:
#    - Check every possible pair of numbers.
#    - Time Complexity: O(n^2)
#    - Space Complexity: O(1)
#
# 2) Efficient:
#    - Use a hash map to store visited numbers and their indices.
#    - For each number, check if its complement (target - num) exists in the map.
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)
# ------------------------------------------------------------

# 🧪 Brute Force Implementation
def twoSum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# ⚡ Efficient Implementation
def twoSum_efficient(nums: list[int], target: int) -> list[int]:
    num_of_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_of_index:
            return [num_of_index[complement], i]
        num_of_index[num] = i
