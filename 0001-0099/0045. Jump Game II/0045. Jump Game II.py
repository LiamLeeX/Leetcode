from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Edge case: if array length is 1, we're already at the end
        if len(nums) <= 1:
            return 0

        jumps = 0  # number of jumps taken
        current_max = 0  # furthest index we can currently reach
        next_max = 0  # furthest index we can reach with one more jump

        # We only need to look until the second-to-last element
        # because if we can reach the last element, we're done
        for i in range(len(nums) - 1):
            # Update the furthest we can reach
            next_max = max(next_max, i + nums[i])

            # If we've reached our current furthest position,
            # we must take a jump
            if i == current_max:
                jumps += 1
                current_max = next_max

                # If we can already reach the end, we're done
                if current_max >= len(nums) - 1:
                    break

        return jumps


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_max = next_max = 0
        # 因为我们最多只可能从len(num)-2处起跳，我们既然已经到达了最后一个数字，那么根本不需要再跳也就不需要遍历
        for i in range(len(nums) - 1):
            next_max = max(next_max, i + nums[i])
            if i == current_max:
                jumps += 1
                current_max = next_max
                if current_max >= len(nums) - 1:
                    return jumps
        return 0 #处理 nums 长度为0的情况

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_max = next_max = 0
        for i in range(len(nums) - 1):
            next_max = max(next_max, i + nums[i])
            if i == current_max:
                jumps += 1
                current_max = next_max
                if current_max >= len(nums) - 1:
                    return jumps
        return 0

# -----
# 算法核心思想：统计一段数组这个范围内我们最远能跳到多少，直到到达我们不得不跳的地方，往前跳一步，
# 重复这个过程

# why  for i in range(len(nums) - 1):?
# We only need to calculate jumps up to the second-to-last position,
# because the goal is to reach the last index.
# Once you’ve reached—or know you can reach—the last index,
# there’s no need for additional processing.
#
# No jump is needed from the last index.
# Jumping from the last index to somewhere beyond is meaningless in this context.
# As soon as you land on (or pass) the last index, you’ve solved the problem.
#
# Greedy boundary updates are completed by the time you reach the second-to-last index.
# Each iteration’s main purpose is to track the farthest reach (farthest) from
# any position in the current window and increment the jump count once you pass the boundary (current_end).
# By the time i is at len(nums) - 2, you’ll have the information needed for the final jump to
# reach the last index.
