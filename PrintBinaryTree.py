print("Constructing Binary Tree...")


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_pre_order(node: TreeNode) -> None:
    if node:
        print(node.value, end=" ")
        print_tree_pre_order(node.left)
        print_tree_pre_order(node.right)


def print_tree_in_order(node: TreeNode) -> None:
    if node:
        print_tree_in_order(node.left)
        print(node.value, end=" ")
        print_tree_in_order(node.right)


def print_tree_post_order(node: TreeNode) -> None:
    if node:
        print_tree_post_order(node.left)
        print_tree_post_order(node.right)
        print(node.value, end=" ")


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

print("Printing tree using pre-order traversal..")
print_tree_pre_order(root)

print("\nPrinting tree using in-order traversal..")
print_tree_in_order(root)

print("\nPrinting tree using post-order traversal..")
print_tree_post_order(root)
