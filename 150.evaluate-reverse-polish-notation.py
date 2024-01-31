#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(c))

        return stack.pop()

# @lc code=end
