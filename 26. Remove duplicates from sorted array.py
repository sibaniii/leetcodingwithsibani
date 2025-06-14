"""PROMBLEM:Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.
Example: Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

# THE CODE WHICH I WROTE
class Solution(object):
    def removeDuplicates(self, nums):
        k = len(nums)                      #stores the initial length of the list in variable k
        i = 0                              #pointer i starts at index 0
        while i < len(nums):               #outer loop runs until the end of the modified nums list
            j = i + 1                      #for each i, j starts from the next index
            while j < len(nums):           #inner loop checks all elements after i
                if nums[i] == nums[j]:     #if a duplicate is found
                    nums.pop(j)            #remove the duplicate element
                    k -= 1                 #decrease the count of unique elements
                else:
                    j += 1                 #only move j forward if no deletion (since deletion shifts elements)
            i += 1                         #move to the next index in outer loop
        return k                           #return count of unique elements

"""Time Complexity: O(n³) in the worst case (when no duplicates) 
-----------------> there are many better codes with better time complexity , this i wrote with whatever knowledge i had , might rewrite later.
Space Complexity: O(1)"""
