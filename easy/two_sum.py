class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = list()
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                l.append(nums.index(d[nums[i]]))
                l.append(i)
                return l
            else:
                d[target-nums[i]] = nums[i]