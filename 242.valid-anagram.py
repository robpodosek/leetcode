#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)

        for c in s:
            chars[c] += 1
        for c in t:
            chars[c] -= 1

        for val in chars.values():
            if val != 0:
                return False

        return True

# @lc code=end
