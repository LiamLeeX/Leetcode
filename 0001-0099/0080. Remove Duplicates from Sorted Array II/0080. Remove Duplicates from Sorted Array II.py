class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        w_pos = 2


        for r_pos in range(2, len(nums)):
            # 想象你在整理一叠扑克牌，规则是每个数字最多出现两次。
            # 你会把整理好的牌放在左边（k指向的位置），未整理的在右边。
            # 当你检查新的牌时，你应该和已经整理好的牌比较（nums[w_pos-2]），
            # 而不是和还没整理的牌比较（nums[r_pos-2]）。
            # 这就是为什么 要用w_pos-2
            if nums[r_pos] != nums[w_pos-2]:
                nums[w_pos] = nums[r_pos]
                w_pos += 1

        return w_pos

#Time O(n)
#Space O(1)

from typing import List



so = Solution()
so.removeDuplicates([1,1,1,2,2,3])