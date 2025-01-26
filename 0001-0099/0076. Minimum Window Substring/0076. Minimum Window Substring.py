import bisect
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window, formed, left, start, min_len = collections.Counter(t), collections.Counter(), 0, 0, 0, len(s) + 1
        for right, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                formed += 1
            while formed == len(need):
                if right - left + 1 < min_len:
                    min_len, start = right - left + 1, left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return s[start:start + min_len % (len(s) + 1)]


so = Solution()
so.minWindow("ADOBECODEBANC", "ABC")
