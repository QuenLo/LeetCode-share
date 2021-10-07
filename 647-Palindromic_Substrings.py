class Solution:
    def countSubstrings(self, s: str) -> int:
        
        s_len = len(s)
        ans = 0
        
        if s_len <= 0: return 0
        
        dp = [ [False]*s_len for i in s ]
        
        # one
        for i in range(s_len):
            dp[i][i] = True
            ans += 1
        
        # two
        for i in range(s_len-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]: ans += 1
        
        # over
        for L in range(2,s_len):
            for i in range( s_len-L ):
                dp[i][i+L] = dp[i+1][i+L-1] and (s[i] == s[i+L])
                if dp[i][i+L]: ans += 1
        
        return ans
