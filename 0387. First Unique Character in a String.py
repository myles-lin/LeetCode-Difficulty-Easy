class Solution:
    def firstUniqChar(self, s: str) -> int:
        cMap = {}
        for c in s:
            if c in cMap:
                cMap[c] += 1
            else:
                cMap[c] = 1

        for i, c in enumerate(s):
            if cMap[c] == 1:
                return i

        return -1

# s = "leetcode" # Output: 0
# s = "loveleetcode" # Output: 2
# s = "aabb" # Output: -1
# Solution().firstUniqChar(s)
