from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root: TreeNode):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def postorder(root: TreeNode):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


def levelorder(root: TreeNode):
    if not root:
        return

    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            print(node.val, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)),
                TreeNode(7, None, TreeNode(9)))

print("pre-order: ", end="")
preorder(root)
print("\nin-order: ", end="")
inorder(root)
print("\npost-order: ", end="")
postorder(root)
print("\nlevel-order: ", end="")
levelorder(root)
