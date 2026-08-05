class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > len(ans):
                        ans = substring

        return ans
