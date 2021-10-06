class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")  # split返回列表
        version2 = version2.split(".")
        for i in range(max(len(version1), len(version2))):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0


from itertools import zip_longest
class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = list(map(int, version1.split(".")))
        versions2 = list(map(int, version2.split(".")))

        for v1, v2 in zip_longest(versions1, versions2, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
