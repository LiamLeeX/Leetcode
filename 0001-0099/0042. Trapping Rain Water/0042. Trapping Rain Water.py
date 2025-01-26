from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = water = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water
# Time O(n)
# Space O(1)