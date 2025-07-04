class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        n = len(s)
        
        for i in range(n):
            seen = set()
            current_len = 0
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                current_len += 1
            max_len = max(max_len, current_len)
        
        return max_len
