class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

# Slow and fast start as the head node
# Always make a dummy node that points to the head, this can help be an
# auxiliary node in certain situations
slow, fast, dummy = head, head, ListNode(0, head)

# slow node advances by one, fast node advances by 2
while fast and fast.next:
    # print(f"slow: {slow.val}")
    # print(f"fast: {fast.val}")
    slow = slow.next
    fast = fast.next.next

#        d h     s     f
# after: 0-1-2-3-4-5-6-7
print("dummy: " + str(dummy.val))
print("head : " + str(head.val))
print("slow : " + str(slow.val))
print("fast : " + str(fast.val))
