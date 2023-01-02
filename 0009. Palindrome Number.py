class Solution:
    def isPalindrome(self, x: int) -> bool:
        result  = str(x)[::-1]
        if result == str(x):
            return True
        else:
            return False
        
# x = 121
# Solution().isPalindrome(x)
