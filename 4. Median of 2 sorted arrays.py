"""PROMBLEM:Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example: Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""

# THE CODE WHICH I WROTE
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)                          #merges both arrays and sorts them
        n = len(merged)                                         #stores the total length of the merged array in variable n
        if n % 2 == 1:                                          #checks if the length is odd
            return merged[n // 2]                               #if odd, return the middle element
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0  #if even, return average of two middle elements

""" Time Complexity: O(n log n)
Space Complexity: O(n)"""
