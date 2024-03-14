#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy is a placeholder where dummy.next always stays pointed to the head of the list while curr advances
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next  # we used up the list1 node so advance it
            else:
                curr.next = list2
                list2 = list2.next  # we used up the list2 node so advance it
            curr = curr.next  # always advance the current node pointer

        curr.next = list1 if list1 else list2

        return dummy.next

# @lc code=end
