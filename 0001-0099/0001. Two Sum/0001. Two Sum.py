from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 如果是个空的花括号创建的就是dict  {1}就是set 验证print(type(seen))
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i
        # If no solution is found (which shouldn't happen given the problem constraints)
        return []
    
# Time: O(n) Each lookup in the table costs only O(1)
# Space: Worst O(n)