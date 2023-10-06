class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3: return n-1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4,n+1):
            cur = 0
            for j in range(1,i//2+1):
                cur = max(cur,dp[j]*dp[i-j])
            dp[i] = cur
        return dp[n]
