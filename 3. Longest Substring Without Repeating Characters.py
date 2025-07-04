class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0                    # initialize variable to keep track of max substring length
        n = len(s)                     # get the length of the input string
        
        for i in range(n):             # start index of the substring
            seen = set()               # set to store characters in the current substring
            current_len = 0            # length of the current substring without repeats
            for j in range(i, n):      # end index of the substring
                if s[j] in seen:       # if character is already in the set, stop expanding substring
                    break
                seen.add(s[j])         # add current character to the set
                current_len += 1      # increase current substring length by 1
            max_len = max(max_len, current_len)  # update max_len if current substring is longer
        
        return max_len                 # return the length of the longest substring without repeating chars


