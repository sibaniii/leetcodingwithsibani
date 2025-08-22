import re
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if re.match(needle, haystack[i:]):
                return i
        return -1
