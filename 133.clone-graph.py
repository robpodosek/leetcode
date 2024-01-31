#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            # Return existing node
            if node in oldToNew:
                return oldToNew[node]

            # Create new copy
            copy = Node(node.val)
            oldToNew[node] = copy

            # Copy new neighbors to new node
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node) if node else None

# @lc code=end
