class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# num = 16 # Output: 4
# Solution().isPerfectSquare(num)
