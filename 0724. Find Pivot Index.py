class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1

# nums = [1,7,3,6,5,6] # Output: 3
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# nums = [1,2,3] # Output: -1
# nums = [2,1,-1] # Output: 0
# Solution().pivotIndex(nums)
