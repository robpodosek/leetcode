#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Make sure there's an even amount
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif not stack or pairs[stack.pop()] != bracket:
                return False

        return not stack


# @lc code=end
