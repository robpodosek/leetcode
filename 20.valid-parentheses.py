#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c not in pairMap:
                stack.append(c)
                continue
            if not stack or stack.pop() != pairMap[c]:
                return False

        return not stack

# @lc code=end
