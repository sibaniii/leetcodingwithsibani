class Solution(object):
    def moveZeroes(self, nums):
        zero=nums.count(0)   
        for a in range(zero):  
            nums.remove(0)           
            nums.append(0)           
        return nums
