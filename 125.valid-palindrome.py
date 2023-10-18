#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        s = s.lower()
        while (start < end):

            # skip past non alphanum
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            # check for mismatch
            if s[start].lower() != s[end].lower():
                return False

            # advance ptrs
            start += 1
            end -= 1
        return True

# @lc code=end
