class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n
        self._reverse(nums, 0, n - 1)  # Reverse the entire array
        self._reverse(nums, 0, k - 1)  # Reverse first k elements
        self._reverse(nums, k, n - 1)  # Reverse remaining elements

    def _reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
