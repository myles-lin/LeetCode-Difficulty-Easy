class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

# nums, target = [-1,0,3,5,9,12], 9 # Output: 4
# nums, target = [-1,0,3,5,9,12], 2 # Output: -1
# Solution().search(nums, target)
