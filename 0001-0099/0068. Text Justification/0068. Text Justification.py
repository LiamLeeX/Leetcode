from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_line_words = []
        current_line_length = 0  # sum of lengths of words (excluding spaces)

        for word in words:
            # Check if adding this word to the current line would exceed maxWidth
            # We use `len(current_line_words)` to account for the minimal space
            # needed between words (which is exactly number_of_words_in_line - 1).
            if current_line_words and current_line_length + len(word) + len(current_line_words) > maxWidth:
                # Justify the current line
                res.append(self.justifyLine(current_line_words, current_line_length, maxWidth, is_last_line=False))
                current_line_words = []
                current_line_length = 0

            current_line_words.append(word)
            current_line_length += len(word)

        # Handle the last line (left-justified)
        last_line = self.justifyLine(current_line_words, current_line_length, maxWidth, is_last_line=True)
        res.append(last_line)

        return res

    def justifyLine(self, words: List[str], current_line_length: int, maxWidth: int, is_last_line: bool) -> str:
        """
        Justify a single line given the list of words, the total chars of these words,
        and whether it is the last line or not.
        """
        # If this is the last line or there is only one word in this line:
        # Left justify (word(s) + single space + trailing spaces).
        if is_last_line or len(words) == 1:
            line = " ".join(words)
            return line + " " * (maxWidth - len(line))

        # Otherwise, fully justify.
        total_spaces = maxWidth - current_line_length
        gaps = len(words) - 1

        # Distribute spaces as evenly as possible.
        # Base number of spaces for each gap.
        base_spaces = total_spaces // gaps
        # Extra spaces assigned to the leftmost gaps first.
        extra_spaces = total_spaces % gaps

        justified_line = []
        for i in range(len(words) - 1):
            # Assign base spaces + 1 if this gap is among the 'extra_spaces'
            space_count = base_spaces + (1 if i < extra_spaces else 0)
            justified_line.append(words[i] + " " * space_count)
        # The last word in the line does not get extra spaces after it (except for trailing if needed,
        # but that’s accounted for in the sum above).
        justified_line.append(words[-1])
        return "".join(justified_line)


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, current_line_words, current_line_length = [], [], 0
        for word in words:
            if current_line_words and current_line_length + len(word) + len(current_line_words) > maxWidth:
                res.append(self.justifyLine(current_line_words, current_line_length, maxWidth, is_last_line=False))
                current_line_words, current_line_length = [], 0
            current_line_words.append(word)
            current_line_length += len(word)
        last_line = self.justifyLine(current_line_words, current_line_length, maxWidth, is_last_line=True)
        res.append(last_line)
        return res

    def justifyLine(self, words: List[str], current_line_length: int, maxWidth: int, is_last_line: bool) -> str:
        if is_last_line or len(words) == 1:
            line = " ".join(words)
            return line + " " * (maxWidth - len(line))
        total_spaces = maxWidth - current_line_length
        base_spaces = total_spaces // (len(words) - 1)
        extra_spaces = total_spaces % (len(words) - 1)
        justified_line = []
        for i in range(len(words) - 1):
            space_count = base_spaces + (1 if i < extra_spaces else 0)
            justified_line.append(words[i] + " " * space_count)
        justified_line.append(words[-1])
        return "".join(justified_line)


so = Solution()
so.fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], 20)
