from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, max_len = set(nums), 0
        for start in nums:
            if start - 1 not in nums:  # 说明是最小的元素了
                end = start + 1
                while end in nums:
                    end += 1
                max_len = max(max_len, end - start)
        return max_len
