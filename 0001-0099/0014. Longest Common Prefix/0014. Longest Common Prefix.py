from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            if any(i == len(strs[j]) or strs[0][i] != strs[j][i] for j in range(1, len(strs))):
                return strs[0][:i]
        return strs[0]

# Time O(s)  S 是所有字符串中的字符总数
# O(1)

so = Solution()
so.longestCommonPrefix(["ab", "a"])
