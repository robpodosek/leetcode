#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.84%)
# Likes:    28030
# Dislikes: 1659
# Total Accepted:    2.8M
# Total Submissions: 8.3M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        result = ""
        for i in range(len(s)):
            oddLen = expand(i, i)
            if len(oddLen) > len(result):
                result = oddLen

            evenLen = expand(i, i + 1)
            if len(evenLen) > len(result):
                result = evenLen

        return result
# @lc code=end
