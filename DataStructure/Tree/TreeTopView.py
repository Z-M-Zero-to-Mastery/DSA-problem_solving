# Given a pointer to the root of a binary tree, print the top view of the binary tree.

# The tree as seen from the top the nodes, is called the top view of the tree.

# For example :

#    1
#     \
#      2
#       \
#        5
#       /  \
#      3    6
#       \
#        4
# Top View : 1 -> 2 -> 5 -> 6

# Explaination: The nodes of the tree are printed from left to right in a level order fashion. Note that the first node of every level is to be printed from top to bottom.


# Solution: 1 (Using Recursion)
def topView(root):
    # Write your code here
    d = {}

    # This function will traverse the tree in a preorder fashion and store the first node of every level in a dictionary
    def traverse(root, key, lvl):
        # Base Case
        if root:
            # If the key is not present in the dictionary then add it to the dictionary with the current level
            # eg: 1 -> 2 -> 5 -> 6
            # d = {0: [1, 0], -1: [2, 1], -2: [5, 2], -3: [6, 3]}
            if key not in d:
                d[key] = [root, lvl]

            # If the key is present in the dictionary then check if the current level is less than the level of the key in the dictionary
            # If yes then update the dictionary with the current level and the root node of the current level
            # eg: 1 -> 2 -> 5 -> 6
            # d = {0: [1, 0], -1: [2, 1], -2: [5, 2], -3: [6, 3]}
            elif d[key][1] > lvl:
                d[key] = [root, lvl]

            # Traverse the left and right subtree with the key as key - 1 and key + 1 respectively and the level as level + 1
            # eg: 1 -> 2 -> 5 -> 6
            # d = {0: [1, 0], -1: [2, 1], -2: [5, 2], -3: [6, 3]}
            # d = {0: [1, 0], -1: [2, 1], -2: [5, 2], -3: [6, 3], 1: [3, 1]}
            traverse(root.left, key - 1, lvl + 1)
            traverse(root.right, key + 1, lvl + 1)

    traverse(root, 0, 0)

    # Print the nodes in the dictionary in sorted order
    for i in sorted(d):
        # Print the root node of every level
        print(d[i][0], end=" ")


# Solution: 2
def topView(root):
    # Write your code here
    if root is None:
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)

    while len(q):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.info
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)
        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)
        q.pop(0)

    for i in sorted(m):
        print(m[i], end=" ")
