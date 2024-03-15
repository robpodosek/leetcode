#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root will be None if its parent was a leaf node
        if not root:
            return None

        # recursively swap the left and right sub-tree nodes
        root.left, root.right = root.right, root.left  # python ftw
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# @lc code=end
