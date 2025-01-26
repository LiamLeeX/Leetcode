class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n -1
        k = m + n - 1
        while j>=0: # 我们需要确保的是nums2 完全合并到 nums1中
            if i>=0 and nums1[i] > nums2[j]: # nums1还没处理完毕 而且 nums1当前数字更大
                nums1[k] = nums1[i]
                i-=1  # 必须要先处理完nums1 
            else:  # nums1处理完毕 或者 nums2当前数字更大
                nums1[k] = nums2[j]
                j-=1
            k-=1
# 处理完nums1再处理nums2
# Time O(m+n) 
# Space O(1)