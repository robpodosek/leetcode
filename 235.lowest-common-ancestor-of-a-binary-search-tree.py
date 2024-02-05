#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Compare p, q values to curr node
# Base case: one is in left, other in right subtree, then curr is LCA;


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time, Space Complexity: O(log n), O(1)
        curr = root

        while q:

            if p.val > curr.val and q.val > curr.val:
                # Traverse right subtree
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                # Traverse left subtree
                curr = curr.left
            else:
                # This means a split occurs or curr is either p or q
                return curr

# @lc code=end
