class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = t[i]
            elif sMap[s[i]] != t[i]:
                return False
            if t[i] not in tMap:
                tMap[t[i]] = s[i]
            elif tMap[t[i]] != s[i]:
                return False
        return True

# s, t = "egg", "add" # Output: true
# s, t = "foo", "bar" # Output: false
# s, t = "paper", "title" #Output: true
# Solution().isIsomorphic(s, t)
