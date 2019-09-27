class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        end = len(nums)-1
        begin = 0
        while(end > begin):
            if end - begin == 1:
                sum += min(nums[begin],nums[end])
            else:
                sum += min(nums[begin],nums[begin+1]) + min(nums[end-1],nums[end])
            end -= 2
            begin += 2
        return sum