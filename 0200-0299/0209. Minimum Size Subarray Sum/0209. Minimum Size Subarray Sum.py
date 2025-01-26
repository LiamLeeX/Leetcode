import bisect
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, total, min_len = 0, 0, 0, len(nums) + 1
        while r < len(nums):
            total += nums[r]
            r += 1
            while total >= target:
                min_len = min(min_len, r - l)
                total -= nums[l]
                l += 1
        return min_len % (len(nums) + 1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums,min_len  = [0] * (len(nums) + 1),len(nums)+1
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        min_length = len(nums) + 1
        
        for i in range(len(nums) + 1):
            # We need prefix_sums[j] - prefix_sums[i] >= target
            # So, prefix_sums[j] >= target + prefix_sums[i]
            required = target + prefix_sums[i]
            # Binary search for the smallest j such that prefix_sums[j] >= required
            j = bisect.bisect_left(prefix_sums, required)
            if j <= len(nums):
                min_length = min(min_length, j - i)
        
        return min_len % (len(nums) + 1)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums,min_len  = [0] * (len(nums) + 1),len(nums)+1
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]        
        for i in range(len(nums) + 1):
            required = target + prefix_sums[i]
            j = bisect.bisect_left(prefix_sums, required)
            if j <= len(nums):
                min_len = min(min_len, j - i)
        return min_len % (len(nums) + 1)
so = Solution()
so.minSubArrayLen(7,[2,3,1,2,4,3])