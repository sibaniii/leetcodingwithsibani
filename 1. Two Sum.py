"""PROMBLEM: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example: Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

# THE CODE WHICH I WROTE
class Solution:
    def twoSum(self, nums, target):
        b = len(nums)                                   #storing the array length in variable b
        for i in range(b):                              #loop starts from 0 till the last elem of nums
            for j in range(i + 1, b):                   #for each i,another loop starts from i+1 - this ensures that 2 same elements arent compared twice
                if nums[i] + nums[j] == target:         #for every [i,j] pair, the code checks if nums[i]+nums[j]==target
                    return [i, j]

""" Time Complexity:- This approach uses two nested loops, so its time complexity is O(n²).
Space Complexity:- O(1) """
