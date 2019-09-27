class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for index in range(len(nums)):
            if nums[index] > target:
                return index
        return len(nums)
        