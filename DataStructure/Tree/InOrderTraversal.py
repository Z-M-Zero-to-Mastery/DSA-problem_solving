# In this challenge, you are required to implement inorder traversal of a tree.

# Complete the inOrder function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.

# Input Format
# Our hidden tester code passes the root node of a binary tree to your inOrder function.

# Output Format
# Print the tree's inorder traversal as a single line of space-separated values.

# Sample Input
# 1
#  \
#   2
#    \
#     5
#    /  \
#   3    6
#    \
#     4

# Sample Output
# 1 2 3 4 5 6


# Solution 1 - Recursive
def inOrder(root):
    # Write your code here
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)


# Solution 2 - Iterative
def inOrder(root):
    # Write your code here
    stack = []
    current = root

    while True:
        # Reach the left most Node of the current Node
        if current:
            # Place pointer to a tree node on the stack
            stack.append(current)
            current = current.left
        # BackTrack from the empty subtree and visit the Node at the top of the stack
        elif stack:
            # If the stack is not empty then pop the top stack element and print it
            current = stack.pop()
            # It will print the node in the order left -> root -> right
            print(current.info, end=" ")
            current = current.right
        else:
            break
