from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = sorted(strs)

        prefix = ""

        first_word = words[0]
        last_word = words[-1]

        for char in first_word:
            if last_word.startswith(prefix+char):
                prefix += char
            else:
                break

        return prefix


s = Solution()
print("1 - " + s.longestCommonPrefix(["ABC", "flower", "flow", "flight"]))
print("2 - " + s.longestCommonPrefix(["flower", "flow", "flight"]))
print("3 - " + s.longestCommonPrefix(["dog", "", "racecar", "car"]))
print("4 - " + s.longestCommonPrefix(["reflower","flow","flight"]))
print("5 - " + s.longestCommonPrefix(["","b"]))
print("6 - " + s.longestCommonPrefix(["a"]))