# Given pointers to the head nodes of 2 linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's data value.
# Note: After the merge point, both lists will share the same node pointers.
#
# Example
# # List1 = 1 -> 2 -> 3 -> NULL
# # List2 = 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# # Merge Node = 3

# Diagram:
# a -> b -> c
#       \
#        d -> e -> f
#       /
# g -> h

# Test Case:
# 1
#  \
#   2 -> 3 -> NULL
#  /
# 1

# Test Case:
# 1 -> 2 -> 3 -> NULL
#  \
#   2 -> 3 -> NULL
#  /
# 1


# Solution: 1
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2

    # Do till the two nodes are the same
    # We also check for the case where the two lists do not merge
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> NULL
    # In this case, the while loop will break when current1 and current2 are both NULL
    # We return -1 in this case
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, the while loop will break when current1 and current2 are both 3
    while current1 != current2:
        # If current1 is NULL, we set it to head2
        # eg 1 -> 2 -> 3 -> NULL
        #    4 -> 5 -> 6 -> 3 -> NULL
        # In this case, current1 will be NULL after 3 -> NULL
        # We set current1 to head2, which is 4 -> 5 -> 6 -> 3 -> NULL
        # We then move current1 to 5
        if current1.next is None:
            current1 = head2
        else:
            current1 = current1.next

        # If current2 is NULL, we set it to head1
        # eg 1 -> 2 -> 3 -> NULL
        # 1 -> 2 -> 3 -> NULL
        if current2.next is None:
            current2 = head1
        else:
            current2 = current2.next

    # If current1 and current2 are both NULL, we return -1
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> NULL
    # In this case, the while loop will break when current1 and current2 are both NULL
    # We return -1 in this case
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, the while loop will break when current1 and current2 are both 3
    # We return 3 in this case
    return current1.data


# Solution: 2 (Using Hash Table)
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2

    # We create a hash table
    # We store the nodes of list1 in the hash table
    # We then traverse list2
    # If the node is in the hash table, we return the node
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, we store 1, 2, 3 in the hash table
    # We then traverse list2
    # When we reach 3, we check if 3 is in the hash table
    # Since 3 is in the hash table, we return 3
    hash_table = {}
    while current1 is not None:
        hash_table[current1] = current1.data
        current1 = current1.next

    while current2 is not None:
        if current2 in hash_table:
            return current2.data
        current2 = current2.next

    return -1


# Solution: 3 (Using Stack)
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2

    # We create two stacks
    # We store the nodes of list1 in stack1
    # We store the nodes of list2 in stack2
    # We then pop the nodes from the stack
    # If the nodes are the same, we return the node
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, we store 1, 2, 3 in stack1
    # We store 4, 5, 6, 3 in stack2
    # We then pop 3 from both stacks
    # Since 3 is the same, we return 3
    stack1 = []
    stack2 = []
    while current1 is not None:
        stack1.append(current1)
        current1 = current1.next

    while current2 is not None:
        stack2.append(current2)
        current2 = current2.next

    while stack1 and stack2:
        node1 = stack1.pop()
        node2 = stack2.pop()

        if node1 == node2:
            return node1.data

    return -1


# Solution: 4 (Using Length)
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2

    # We find the length of list1
    # We find the length of list2
    # We find the difference between the length of list1 and list2
    # We then traverse the list with the longer length
    # We move the pointer of the longer list by the difference
    # We then traverse both lists
    # If the nodes are the same, we return the node
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, we find the length of list1 to be 3
    # We find the length of list2 to be 4
    # The difference is 1
    # We move the pointer of list2 by 1
    # We then traverse both lists
    # When we reach 3, we return 3
    length1 = 0
    length2 = 0
    while current1 is not None:
        length1 += 1
        current1 = current1.next

    while current2 is not None:
        length2 += 1
        current2 = current2.next

    difference = abs(length1 - length2)

    current1 = head1
    current2 = head2
    if length1 > length2:
        for i in range(difference):
            current1 = current1.next
    else:
        for i in range(difference):
            current2 = current2.next

    while current1 is not None and current2 is not None:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next

    return -1


# Solution: 5 (In an modular way)
def findMergeNode(head1, head2):
    def getLength(head):
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        return length

    def getNode(d, head1, head2):
        current1 = head1
        current2 = head2

        for i in range(d):
            current1 = current1.next

        while current1 is not None and current2 is not None:
            if current1 == current2:
                return current1.data
            current1 = current1.next
            current2 = current2.next

        return -1

    length1 = getLength(head1)
    length2 = getLength(head2)

    difference = abs(length1 - length2)

    if length1 > length2:
        return getNode(difference, head1, head2)
    else:
        return getNode(difference, head2, head1)


# Solution: 6 (Using Recursion)
def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2

    # We traverse list1
    # If current1 is NULL, we return head2
    # We traverse list2
    # If current2 is NULL, we return head1
    # We then traverse both lists
    # If the nodes are the same, we return the node
    # eg 1 -> 2 -> 3 -> NULL
    #    4 -> 5 -> 6 -> 3 -> NULL
    # In this case, we traverse list1
    # When we reach 3 -> NULL, we return head2, which is 4 -> 5 -> 6 -> 3 -> NULL
    # We traverse list2
    # When we reach 3 -> NULL, we return head1, which is 1 -> 2 -> 3 -> NULL
    # We then traverse both lists
    # When we reach 3, we return
    def traverse(current1, current2):
        if current1 is None:
            return head2
        if current2 is None:
            return head1

        return traverse(current1.next, current2.next)

    current1 = traverse(current1, current2)
    current2 = traverse(current2, current1)

    while current1 is not None and current2 is not None:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next

    return -1


# Solution: 7
def findMergeNode(head1, head2):
    temp1 = head1
    temp2 = head2

    # We traverse list1
    while temp1 != None:
        # We traverse list2
        # If the nodes are the same, we return the node
        # Here we are again assinging temp2 to head2 to traverse list2 again
        temp2 = head2
        # This inner loop will first check all the nodes of list2 with the first node of list1
        while temp2 != None:
            if temp1 == temp2:
                return temp2.data

            else:
                temp2 = temp2.next

        # We then move temp1 to the next node
        if temp1 == temp2:
            return temp1.data

        else:
            temp1 = temp1.next
