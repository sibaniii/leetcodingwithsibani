"""PROMBLEM:You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example: Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]."""

# THE CODE WHICH I WROTE
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)                   # get the length of the digits list
        for i in range(n - 1, -1, -1):   # iterate backwards from last digit to first
            if digits[i] < 9:            # if current digit is less than 9
                digits[i] += 1           # add one to this digit
                return digits            # return the list immediately (no carry needed)
            digits[i] = 0               # if digit was 9, set it to 0 (carry the 1 to next digit)
        return [1] + [0] * n             # if all digits were 9, result is 1 followed by n zeros


""" Time Complexity: O(n)
    Space Complexity: O(n)"""
