import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        each_word_len = len(words[0])
        word_count = len(words)
        substring_len = each_word_len * word_count
        word_counter = collections.Counter(words)
        result = []

        # Loop over all possible starting points for the substring
        for i in range(each_word_len):
            left = i
            right = i
            window_map = collections.Counter()

            # Slide through the string in steps of word_len
            while right + each_word_len <= len(s):
                word = s[right:right + each_word_len]
                right += each_word_len

                if word in word_counter:
                    window_map[word] += 1

                    # If there are more of the word than we need, shift left
                    while window_map[word] > word_counter[word]:
                        left_word = s[left:left + each_word_len]
                        window_map[left_word] -= 1
                        left += each_word_len

                    # If the window is valid, record the starting index
                    if right - left == substring_len:
                        result.append(left)
                else:
                    # Reset the window if the word is not in the words list
                    window_map.clear()
                    left = right

        return result


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        each_word_len, word_counter, res = len(words[0]), collections.Counter(words), []
        for i in range(each_word_len):
            left = right = i
            window_map = collections.Counter()
            while right + each_word_len <= len(s):
                word = s[right:right + each_word_len]
                right += each_word_len
                if word in word_counter:
                    window_map[word] += 1
                    while window_map[word] > word_counter[word]:
                        left_word = s[left:left + each_word_len]
                        window_map[left_word] -= 1
                        left += each_word_len
                    if right - left == each_word_len * len(words):
                        res.append(left)
                else:
                    window_map.clear()
                    left = right
        return res


so = Solution()
so.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"])