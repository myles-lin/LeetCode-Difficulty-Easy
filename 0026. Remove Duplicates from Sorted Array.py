class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head = 0
        for i in range(1, len(nums)):
            if nums[head] != nums[i]:
                head += 1
                nums[head]= nums[i]
        return head + 1

# nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Solution().removeDuplicates(nums)
