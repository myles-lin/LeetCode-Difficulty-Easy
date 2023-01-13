class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if nums[mid] < target:
            return mid + 1
        else:
            return mid
    
# nums, target = [1,3,5,6], 5 # Output: 2
# nums, target = [1,3,5,6], 2 # Output: 1
# nums, target = [1], -1 # Output: 0
# Solution().searchInsert(nums, target)
