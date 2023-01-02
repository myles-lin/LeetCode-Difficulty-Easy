class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n[::-1] + (32 - len(n)) * "0"
        return int(n, 2)

# n = 00000010100101000001111010011100 # answer = 964176192
# n = 11111111111111111111111111111101 # answer = 3221225471
# Solution().reverseBits(n)
