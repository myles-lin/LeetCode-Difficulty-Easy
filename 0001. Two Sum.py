class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in tmp_dict:
                tmp_dict[nums[i]] = i
            else:
                return [tmp_dict[target - nums[i]], i]

# nums, target = [2,7,11,15], 9 # Output: [0,1]
# nums, target = [3,2,4], 6 # Output: [1,2]
# nums, target = [3,3], 6 # Output: [0,1]
# Solution().twoSum(nums, target)
