import bisect
import collections


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class Solution:
    def buildMap(self, t: str):
        self.char_indices = collections.defaultdict(list)
        for i, char in enumerate(t):
            self.char_indices[char].append(i)

    def isSubsequence(self, s: str, t: str) -> bool:
        self.buildMap(t)
        curr_pos = 0  # Current position in t
        for char in s:
            pos_list = self.char_indices[char]
            idx = bisect.bisect_left(pos_list, curr_pos)
            if idx == len(pos_list):
                return False
            curr_pos = pos_list[idx] + 1
        return True
    # 目的就是在s中找到一个字符  然后在t中快速找到相同的一个字符并用掉它


so = Solution()
so.isSubsequence(s="abbbbbc", t="xahbbbgbbdbc")
