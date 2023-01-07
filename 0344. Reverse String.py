class Solution:
    def reverseString(self, s: List[str]) -> None:
    # 1.    s.reverse()

    # 2.    for i in range(len(s)//2):
    #         # i + j == len(s) - 1
    #         j = len(s) - 1 - i
    #         tmp = s[i]
    #         s[i] = s[j]
    #         s[j] = tmp

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
