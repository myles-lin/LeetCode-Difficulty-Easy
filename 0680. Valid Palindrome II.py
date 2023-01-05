class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                del_left = s[left+1 : right+1]
                del_right = s[left : right] 
                return del_left == del_left[::-1] or del_right == del_right[::-1]
            left += 1
            right -= 1
        return True

# s = "aba" # Output: true
# s = "abca" # Output: true
# s = "abc" # Output: false
# Solution().validPalindrome(s)
