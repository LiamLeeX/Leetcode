from typing import List


class Solution:
    def _reverse(self, chars: list, start: int, end: int) -> None:
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        # 由于Python中str是不可变的，所以必须使用这种妥协的转换才能O(1) Space
        chars = list(s)
        # Remove extra spaces
        write = 0
        for read in range(len(chars)):
            if chars[read] != " " or (write > 0 and chars[write - 1] != " "):
                chars[write] = chars[read]
                write += 1

        # Remove trailing spaces
        while write > 0 and chars[write - 1] == " ":
            write -= 1

        # Reverse the entire string
        self._reverse(chars, 0, write - 1)

        # Reverse each word
        start = 0
        for end in range(write):
            if end == write - 1 or chars[end + 1] == " ":
                self._reverse(chars, start, end)
                start = end + 2

        return "".join(chars[:write])


class Solution:
    def _reverse(self, chars: list, start: int, end: int) -> None:
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        chars, write = list(s), 0
        for read in range(len(chars)):
            if chars[read] != " " or (write > 0 and chars[write - 1] != " "):
                chars[write] = chars[read]
                write += 1
        while write > 0 and chars[write - 1] == " ":
            write -= 1
        self._reverse(chars, 0, write - 1)
        start = 0
        for end in range(write):
            if end == write - 1 or chars[end + 1] == " ":
                self._reverse(chars, start, end)
                start = end + 2
        return "".join(chars[:write])


so = Solution()
# so.reverseWords("   the sky is blue  ")
so.reverseWords("  hello world  ")
