# Runtime 63 ms, Memory 13.9 MB
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        number = 0
        for i in range(n):
            score = ord(columnTitle[i]) - 64
            number += score * pow(26, n-i-1)

        return number

# columnTitle = "AB" # answer = 28
# columnTitle = "ZY" # answer = 701
# Solution().titleToNumber(columnTitle)
