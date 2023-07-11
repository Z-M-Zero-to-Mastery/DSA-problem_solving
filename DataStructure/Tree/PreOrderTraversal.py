# Complete the preOrder function in the editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

# Input Format
# Our hidden tester code passes the root node of a binary tree to your preOrder function.

# Output Format
# Print the tree's preorder traversal as a single line of space-separated values.

# Sample Input
# 1
#  \
#   2
#    \
#     5
#   /  \
#  3    6
#   \
#    4

# Sample Output
# 1 2 5 3 4 6

# Explanation
# The required result of the preorder traversal of the given binary tree is as above.


# Class for a node of the tree
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# *******************************************************************************************

# Solution 1: Recursive


def preOrder(root):
    # eg : 1 2 5 3 4 6
    if root:
        # print the root node
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)


# Solution 2: Iterative


def preOrder(root):
    # eg : 1 2 5 3 4 6
    stack = []
    stack.append(root)

    while stack:
        # pop the top node
        node = stack.pop()
        # print the node
        print(node.info, end=" ")
        # push the right node first
        if node.right:
            stack.append(node.right)
        # push the left node
        if node.left:
            stack.append(node.left)


# *******************************************************************************************

# Input
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
