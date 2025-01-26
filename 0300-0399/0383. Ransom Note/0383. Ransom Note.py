import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_counter = collections.Counter(magazine)
        for char in ransomNote:
            if char not in char_counter or char_counter[char] == 0:
                return False
            char_counter[char] -= 1
        return True