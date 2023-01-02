# Runtime 162 ms, Memory 15.5 MB
class Solution:
    def majorityElement(self, nums: int) -> int:
        nums.sort()
        return nums[len(nums)//2]

# nums = [3,2,3] # answer = 3
# nums = [2,2,1,1,1,2,2] # answer = 2
# Solution().majorityElement(nums)
