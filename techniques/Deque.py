# Stack
from collections import deque


print("=== deque used as a stack ===")
s = deque()
s.append(1)
print(s)
s.append(2)
print(s)
s.append(3)
print(s)
s.pop()
print(s)
s.pop()
print(s)

# Queue
print("=== deque used as a queue ===")
q = deque()
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.popleft()
print(q)
q.popleft()
print(q)

# LinkedList
print("=== deque used as a linked list ===")
ll = deque()
ll.append(1)
print(ll)
ll.append(2)
print(ll)
ll.appendleft(0)
print(ll)
ll.pop()
print(ll)
ll.popleft()
print(ll)
