class Solution(object):
    def removeDuplicates(self, nums):
        k = len(nums)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                    k -= 1
                else:
                    j += 1
            i += 1
        return k
