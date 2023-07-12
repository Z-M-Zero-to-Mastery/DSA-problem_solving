# Complete the postOrder function in the editor below. It received 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's postorder traversal as a single line of space-separated values.

# Input Format

# Our hidden tester code passes the root node of a binary tree to your postOrder function.

# Output Format

# Print the tree's postorder traversal as a single line of space-separated values.

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

# 4 3 6 5 2 1

# Explanation

# The postorder traversal is shown.

# Solution:


# Recursive Approach
def postOrder(root):
    # Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")


# Iterative Approach
def postOrder(root):
    # Write your code here
    stack = []
    result = []
    node = root

    # We are using two stacks here to store the nodes and the result respectively
    # We are using the result stack to store the nodes in the postorder traversal
    # which is left -> right -> root
    # So we are storing the nodes in the result stack in the order root -> right -> left
    while stack or node:
        # This will check if the node is not null
        if node:
            # This will append the node to the stack and the result
            # This will also move the node to the right of the current node
            # This will continue until the node is null
            # eg: 1 -> 2 -> 5 -> 6
            # Here we are appending 1 to the stack and the result and moving to 2 and so on
            # stack = [1, 2, 5, 6] and result = [1, 2, 5, 6]
            # when node = 2 , node.left = null and set node to null and continue
            stack.append(node)
            result.append(node.info)
            node = node.right
        # This will check if the node is null and the stack is not empty
        # This will pop the node from the stack and move to the left of the current node
        else:
            # eg: stack = [1, 2, 5, 6] and result = [1, 2, 5, 6]
            # Here we are popping 6 from the stack and moving to 5 and so on
            # This will continue until the stack is empty
            # node = 6 and stack = [1, 2, 5] and result = [1, 2, 5, 6]
            node = stack.pop()
            # node = 6 , node.left = null and set node to null and continue
            # node = 5 , node.left = null and set node to null and continue
            # node = 2 , node.left = 4 and set node to 4 and continue
            # node = 4 , node.left = null and set node to null and continue
            # node = 1 , node.left = null and set node to null and continue
            node = node.left

    # stack = [] and result = [1, 2, 5, 6, 3, 4]
    # This will print the result in the postorder traversal
    # which is left -> right -> root
    # here *result[::-1] will reverse the result and print it in the postorder traversal
    # result[::-1] = [4, 3, 6, 5, 2, 1]
    print(*result[::-1], sep=" ")
