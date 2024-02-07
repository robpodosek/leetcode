#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (62.33%)
# Likes:    11582
# Dislikes: 849
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
# Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    # Use a Level-Order BFS and take the last node of each level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque([root])

        while q:
            rightSide = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node  # right side will have last node in this current level of the queue
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                result.append(rightSide.val)

        return result

# @lc code=end
