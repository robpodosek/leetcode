print("Constructing Binary Tree...")


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree(node: TreeNode) -> None:
    if node:
        print_tree(node.left)
        print(node.value, end=" ")
        print_tree(node.right)


# Construct a sample binary tree
#        4
#       / \
#      2   6
#     / \ / \
#    1  3 5  7

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Printing Tree...")
print_tree(root)
