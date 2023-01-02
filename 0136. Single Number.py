class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i

        return ans

# nums = [4,1,2,1,2] # answer = 4
# Solution().singleNumber(nums)
