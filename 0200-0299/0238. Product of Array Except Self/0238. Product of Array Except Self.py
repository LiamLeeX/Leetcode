class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize output array with 1s

        # First pass: Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix  # Store running prefix product
            prefix *= nums[i]  # Update prefix for next iteration

        # Second pass: Calculate suffix products and combine
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix  # Multiply existing prefix by suffix
            suffix *= nums[i]  # Update suffix for next iteration

        return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix # 在第一遍的时候只用计算当前数字左侧所有数字的乘积 也就是prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix # 在逆序的时候，由于要得到最终结果，所以要将左侧的乘积 result[i] * 右侧所有数字的积 suffix
            suffix *= nums[i]
        return result