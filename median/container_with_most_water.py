class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                result = max(result, ((right-left) * height[left]))
                left += 1
            else:
                result = max(result,((right-left) * height[right]))
                right -= 1
        return result