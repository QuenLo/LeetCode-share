class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s = [roman_int[x] for x in s]
        ans = 0
        for n in range(len(s)-1):
            if s[n] >= s[n+1]:
                ans += s[n]
            else:
                ans -= s[n]
        ans += s[-1]   
        return (ans)
