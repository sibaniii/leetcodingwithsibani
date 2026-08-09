class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3 = nums1[:m] + nums2
        nums3.sort()
        nums1[:] = nums3
