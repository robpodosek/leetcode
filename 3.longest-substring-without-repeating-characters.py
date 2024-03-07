#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        letters = set()

        for r in range(len(s)):
            # if it's in the letters then this substring is invalid
            while s[r] in letters:
                letters.remove(s[l])
                l += 1

            letters.add(s[r])
            w = r - l + 1
            longest = max(longest, w)

        return longest

# @lc code=end
