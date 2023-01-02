class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        strs = sorted(strs, key=len)
        i = 0
        m = len(strs[0])
        common_prefix = ''
        while i < m:
            tmp = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != tmp:
                    i = m
                    break
                elif j == n - 1:
                    common_prefix += tmp

            i += 1
        return common_prefix

# strs = ["flower","flow","flight"] # answer = "fl"
# strs = ["dog","racecar","car"] # answer = ""
# Solution().longestCommonPrefix(strs)
