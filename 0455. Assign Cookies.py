class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        g = sorted(g)
        s = sorted(s)
        i = len(g) - 1
        j = len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                cnt += 1
                j -= 1
            i -= 1
        return cnt

# g, s = [1,2,3], [1,1] # Output: 1
# g, s = [1,2], [1,2,3] #Output: 2
# Solution().findContentChildren(g, s)
