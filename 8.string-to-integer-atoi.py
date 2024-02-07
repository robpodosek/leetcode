#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i, res, sign, = 0, 0, 1
        MAX_INT, MIN_INT = 2**31 - 1, -2**31

        # whitespace
        while i < len(s) and s[i] == " ":
            i += 1

        # +/- symbol
        if i < len(s) and s[i] == "-":
            i += 1
            sign = -1
        elif i < len(s) and s[i] == "+":
            i += 1

        # check for number
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign

        # Check max/min int
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
# @lc code=end
