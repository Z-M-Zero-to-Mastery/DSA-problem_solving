# The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height 2:
#
#         4
#       /   \
#     2      6
#   /  \    /
# 1     3  5
#

# Return a single integer denoting the height of the binary tree.

# Sample Input
#              3
#            /   \
#           2     5
#         /      /  \
#        1      4    6
#                     \
#                      7
# Sample Output
# 3


# Solution 1
def height(root):
    # Write your code here
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


# Solution 2 (Iterative)
def height(root):
    # Write your code here
    if root is None:
        return -1
    else:
        # Create a queue and add the root to it
        # eg    3
        queue = [root]
        height = -1

        while queue:
            height += 1
            # For each node in the queue, pop it and add its left and right child to the queue
            for _ in range(len(queue)):
                # eg    3
                node = queue.pop(0)
                # eg    2
                if node.left:
                    queue.append(node.left)
                # eg    5
                if node.right:
                    queue.append(node.right)

        return height
