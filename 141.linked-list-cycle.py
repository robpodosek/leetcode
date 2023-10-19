#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head

        while hare and hare.next:
            tortoise = tortoise.next  # moves forward one pace
            hare = hare.next.next    # hops two forwards
            if hare == tortoise:
                return True

        return False

# @lc code=end
