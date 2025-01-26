class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  
        # Iterate through the array, but only up to max_reach
        for i in range(len(nums)):
            # If current position is beyond our reach, return False
            if i > max_reach:
                return False

            # Update max_reach if current position + jump length is greater
            max_reach = max(max_reach, i + nums[i])

            # If we can reach the last index, return True
            if max_reach >= len(nums) - 1:
                return True

        # return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        # return True