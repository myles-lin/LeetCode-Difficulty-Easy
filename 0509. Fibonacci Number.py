class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        dp = [None] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

# n = 2 # Output: 1
# n = 4 # Output: 3
# n = 10 # Output: 55
# Solution().fib(n)
