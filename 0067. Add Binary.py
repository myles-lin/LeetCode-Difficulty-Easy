class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer_demical = int(a, 2) + int(b, 2)
        answer_binary = bin(answer_demical)[2:]
        return answer_binary
