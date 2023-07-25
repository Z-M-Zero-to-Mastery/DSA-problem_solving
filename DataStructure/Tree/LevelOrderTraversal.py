# Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function levelOrder and print the values in a single line separated by a space.

# For example:

#      3
#    /   \
#   5     2
#  / \    /
# 1   4  6

# For the above tree, the level order traversal is 3 -> 5 -> 2 -> 1 -> 4 -> 6.


# Solution 1 - Using Queue
def levelOrder(root):
    # Write your code here
    queue = [root] if root else []

    # while queue is not empty
    # eg 3 5 2 1 4 6
    # first time queue = [3]
    while queue:
        # pop the first element
        node = queue.pop()
        print(node.info, end=" ")

        # if node.left is not None, insert it to the front of the queue
        if node.left:
            queue.insert(0, node.left)
        # if node.right is not None, insert it to the front of the queue
        if node.right:
            queue.insert(0, node.right)


# Solution 2 - Using deque
from collections import deque


def levelOrder(root):
    # Write your code here
    queue = deque([root]) if root else deque([])

    # while queue is not empty
    # eg 3 5 2 1 4 6
    # first time queue = [3]
    while queue:
        # pop the first element
        node = queue.popleft()
        print(node.info, end=" ")

        # if node.left is not None, insert it to the front of the queue
        if node.left:
            queue.append(node.left)
        # if node.right is not None, insert it to the front of the queue
        if node.right:
            queue.append(node.right)
