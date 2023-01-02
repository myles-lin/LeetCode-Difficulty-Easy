class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        y = 0
        while y < len(nums):
            if nums[y] == 0:
                y += 1
            else:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
                y += 1
