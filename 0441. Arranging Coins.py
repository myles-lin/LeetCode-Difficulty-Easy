class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            coins = (1 + mid) * mid / 2
            if coins > n:
                right = mid
            else:
                left = mid + 1
        return left - 1

# n = 5 # Output: 2
# n = 8 # Output: 3
# Solution().arrangeCoins(n)
