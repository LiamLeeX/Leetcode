class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        w_pos = 1
        # 因为当range(1,1)的时候下面的循环事实上并不会执行所以不用判断数组长度为1的情况
        for r_pos in range(1, len(nums)): 
            if nums[r_pos - 1] != nums[r_pos]:
                nums[w_pos] = nums[r_pos]
                w_pos+=1
        return w_pos
    
# Time O(n)
# Space O(1)
