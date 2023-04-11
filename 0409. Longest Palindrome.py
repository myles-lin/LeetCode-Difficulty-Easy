class Solution:
    def longestPalindrome(self, s: str) -> int:
        cMap = {}
        for c in s:
            if c in cMap:
                cMap[c] += 1
            else:
                cMap[c] = 1
        
        res = 0
        for c in cMap:
            res += cMap[c] // 2 * 2
            if res % 2 == 0 and cMap[c] % 2 == 1:
                res += 1

        return res

# s = "abccccdd" # Output: 7
# s = "a" # Output: 1
# Solution().longestPalindrome(s)
