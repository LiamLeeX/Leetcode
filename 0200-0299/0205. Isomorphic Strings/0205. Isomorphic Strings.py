class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t ,t_to_s = {},{}
        for chs, cht in zip(s, t):
            if chs in s_to_t:
                if s_to_t[chs] != cht:
                    return False
            else:
                s_to_t[chs] = cht
            if cht in t_to_s:
                if t_to_s[cht] != chs:
                    return False
            else:
                t_to_s[cht] = chs
        return True


so = Solution()
so.isIsomorphic('title', 'taper')
