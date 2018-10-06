class Solution(object):
    def jianshengzi(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        
        for i in range(4, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        
        return dp[n]