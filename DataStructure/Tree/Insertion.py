# You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

# Sample Input

#         4
#       /   \
#      2     7
#     / \
#    1   3

# The value to be inserted is 6.

# Sample Output

#          4
#       /    \
#      2      7
#     / \    /
#    1   3  6


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Solution: 1 - Iterative
    # Time Complexity: O(h)
    # Space Complexity: O(1)
    def insert(self, val):
        # Here we are checking if the root is None. If it is, we are creating a new node and assigning it to the root.
        if self.root is None:
            self.root = Node(val)
            return self.root

        # Here we are creating two variables called current and parent. We are assigning the root to both of them.
        current = self.root
        parent = self.root

        # Here we are looping through the tree until we find a leaf node. We are doing this by checking if the current is not None. If it is not None, we are assigning the current to the parent and then checking if the value is less than the current value. If it is, we are assigning the current to the left child of the current and if not, we are assigning the current to the right child of the current.
        while current is not None:
            parent = current
            if val < current.info:
                current = current.left
            else:
                current = current.right

        # Here we are checking if the value is less than the parent value. If it is, we are assigning the parent's left child to a new node with the value. If not, we are assigning the parent's right child to a new node with the value.
        if val < parent.info:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

        return self.root

    # or -------------------------

    def insert(self, val):
        # Enter you code here.
        newnode = Node(val)

        # case 1: Tree is empty
        if self.root is None:
            self.root = newnode
            return

        cur = self.root
        while cur:
            # case 2: val is less than current node
            if val < cur.info:
                if cur.left is None:
                    cur.left = newnode
                    return

                cur = cur.left

            # case 3: val is greater than current node
            else:
                if cur.right is None:
                    cur.right = newnode
                    return

                cur = cur.right

    # Solution: 2 - Recursive
    # Time Complexity: O(h)
    # Space Complexity: O(h)
    def insert(self, val):
        # Here we are checking if the root is None. If it is, we are creating a new node and assigning it to the root.
        if self.root is None:
            self.root = Node(val)
            return self.root

        # Here we are calling the insertHelper function with the root and the value.
        self.insertHelper(self.root, val)

        return self.root

    # Here we are checking if the value is less than the current value. If it is, we are checking if the left child is None. If it is, we are assigning the left child to a new node with the value. If not, we are calling the insertHelper function with the left child and the value. If the value is greater than the current value, we are checking if the right child is None. If it is, we are assigning the right child to a new node with the value. If not, we are calling the insertHelper function with the right child and the value.
    def insertHelper(self, current, val):
        if val < current.info:
            if current.left is None:
                current.left = Node(val)
            else:
                self.insertHelper(current.left, val)
        else:
            if current.right is None:
                current.right = Node(val)
            else:
                self.insertHelper(current.right, val)

        return self.root


# Input:
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
