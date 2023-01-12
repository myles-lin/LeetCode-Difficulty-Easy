class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        cnt = 0
        for val in bin(result):
            if val == '1':
                cnt += 1
        return cnt

# x, y = 1, 4 #Output: 2
# Solution().hammingDistance(x, y)
