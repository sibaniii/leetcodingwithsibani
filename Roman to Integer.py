class Solution(object):
    def romanToInt(self, s):
        roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        t=0    #total
        pv=0   #prev value
        
        #iterating from right to left
        for char in reversed(s):   #using pythons builtin func reversed
            value=roman_map[char]
            if value<pv:
                t-=value
            else:
                t+=value
            pv=value
        
        return t
