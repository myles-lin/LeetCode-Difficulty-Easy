from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = defaultdict(int)
        count = 0
        for i in stones:
            stones_dict[i] += 1
        for i in jewels:
            if i in stones_dict.keys():
                count += stones_dict[i]
        return count

# jewels, stones = "aA", "aAAbbbb" # Output: 3
# jewels, stones = "z", "ZZ" # Output: 0
# Solution().numJewelsInStones(jewels, stones)
