import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for s in strs:
            group[tuple(sorted(s))].append(s)
        return list(group.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())
so = Solution()
so.groupAnagrams(["eat","tea","tan","ate","nat","bat"])