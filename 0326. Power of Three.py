class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        i = 3    
        while i < n:
            i *= 3

        if i == n:
            return True

        return False

# n = 27 # True
# n = 0 # False
# n = -1 # False
# Solution().isPowerOfThree(n)
