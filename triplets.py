"""PROMBLEM:Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example: Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter."""

# THE CODE WHICH I WROTE
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)                                                  #stores the length of the input list in variable n
        result = []                                                    #initializes an empty list to store unique triplets

        for i in range(n):                                             #first loop starts from 0 to n-1
            for j in range(i + 1, n):                                  #second loop starts from i+1 to n-1
                for k in range(j + 1, n):                              #third loop starts from j+1 to n-1
                    if nums[i] + nums[j] + nums[k] == 0:               #checks if the sum of the triplet is 0
                        triplet = sorted([nums[i], nums[j], nums[k]])  #sort the triplet to handle duplicates
                        if triplet not in result:                      #check if this triplet is not already in result
                            result.append(triplet)                     #add unique triplet to the result
        return result                                                  #return the final list of unique triplets

""" Time Complexity: O(n³) --------> cause of 3 for nested loops, 
Space Complexity: O(k), where k is the number of unique triplets found """
