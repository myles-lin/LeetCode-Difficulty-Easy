class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[-1] == n - 1:
            return n
        else:
            return (n * (n+1))//2  - sum(nums)
