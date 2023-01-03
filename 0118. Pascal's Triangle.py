# Runtime 58 ms, Memory 13.8 MB
class Solution:
    def generate(self, numRows: int) -> int:
        lst = []
        for i in range(0, numRows):
            lst.append([1] * (i+1))
            for j in range(1, i):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        return lst
        
# numRows = 5 # answer = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# Solution().generate(numRows)
