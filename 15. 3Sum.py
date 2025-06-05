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
        nums.sort()                              #sorts the input list in ascending order
        result = []                              #initializes an empty list to store unique triplets
        for i in range(len(nums)):               #outer loop picks the first element one by one
            if i > 0 and nums[i] == nums[i - 1]:
                continue                         #skips duplicates for the first element to avoid repeated triplets
            left = i + 1                         #sets the left pointer to the next index
            right = len(nums) - 1                #sets the right pointer to the last index
            while left < right:                  #while loop runs as long as left < right
                total = nums[i] + nums[left] + nums[right]  #calculates the sum of three elements
                if total < 0:
                    left += 1                    #if total is less than 0, move left pointer to right to increase the sum
                elif total > 0:
                    right -= 1                   #if total is more than 0, move right pointer to left to decrease the sum
                else:
                    result.append([nums[i], nums[left], nums[right]])  #if total is 0, a valid triplet is found

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1                #skips duplicates for the second element

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1               #skips duplicates for the third element

                    left += 1                    #move left pointer inward
                    right -= 1                   #move right pointer inward

        return result                            #returns the final list of all unique triplets





        
