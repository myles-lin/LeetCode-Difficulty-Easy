# Runtime 1100 ms, Memory 25.9 MB
from collections import defaultdict 
class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        num_cnt = defaultdict(int)
        for i in nums:
            num_cnt[i] += 1
            if num_cnt[i] == 2:
                return True
        return False


# Runtime 497 ms, Memory 26.1 MB
class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        return len(set(nums)) != len(nums)

# nums = [1,1,1,3,3,4,3,2,4,2] # True
# nums = [1,2,3,4] # False
# Solution().containsDuplicate(nums)
