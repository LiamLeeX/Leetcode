from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pos = 0
        for read_pos in range(len(nums)):
            if nums[read_pos] != val:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        return write_pos # 因为只要遇到满足条件的数字 都会+1 所以直接返回write_pos
    
# Time O(n)
# Space O(n)