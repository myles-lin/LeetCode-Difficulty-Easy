class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)
        return t

# s, t = "abcd", "abcde" # Output = "e"
# s, t = "", "y" # Output = "y"
# Solution().findTheDifference(s, t)
