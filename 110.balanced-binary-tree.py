#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def depth(root):
            if root is None:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        l = depth(root.left)
        r = depth(root.right)

        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

# @lc code=end
