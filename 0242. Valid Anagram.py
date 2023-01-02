# Runtime 99 ms, Memory 14.3 MB
from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for i in s:
            dict_s[i] += 1
        for i in t:
            dict_t[i] += 1

        return dict_s == dict_t

# s = "anagram" # True
# t = "nagaram"
# s = "rat" # False
# t = "cat"
# Solution().isAnagram(s, t)
