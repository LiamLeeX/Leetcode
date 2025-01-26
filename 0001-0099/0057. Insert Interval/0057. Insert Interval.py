from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, i = [], 0
        start, end = newInterval
        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result
so  = Solution()
so.insert([[1,3],[6,9]],[2,5])