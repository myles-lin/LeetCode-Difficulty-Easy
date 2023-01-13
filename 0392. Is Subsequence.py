class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        rec = 0
        sRun = 0
        for i in range(len(s)):
            for j in range(rec, len(t)):
                if s[i] == t[j]:
                    rec = j + 1
                    sRun += 1
                    break
        return sRun == len(s)

        # i, j = 0, 0 
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)

# s, t = "abc", "ahbgdc" # Output: true
# s, t = "axc", "ahbgdc" #Output: false
# Solution().isSubsequence(s, t)
