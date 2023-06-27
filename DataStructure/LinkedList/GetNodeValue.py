# Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.

# Example
# # This is a reference to the list: 0 -> 1 -> 2 -> 3
# # 2 is found at position 1 from the tail of the linked list. Return 2.

# Sample Input
# 3
# 1
# 2
# 3
# 1

# Sample Output
# 2

# Explanation
# In the diagram below, the position of 2 from the tail is 1.

# In the second case, the list is 3 -> 2 -> 1 -> NULL. The element with position of 2 from tail contains 3.

# Class for a node of the linked list
import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# The getNode function below.
# It returns the data value of the node at a given position from the tail.

# ********************************************************************************************************


# Solution 1:
def getNode(head, positionFromTail):
    ptr1 = head
    ptr2 = head

    # Here we will move ptr1 to the positionFromTail
    # and then we will move both ptr1 and ptr2 until ptr1 reaches the end of the list
    # eg : 1 -> 2 -> 3 -> 4 -> 5
    # positionFromTail = 3
    # So the value we need to find is 2
    # ptr1 will move to 3
    for i in range(positionFromTail):
        ptr1 = ptr1.next

    # Now we will move both ptr1 and ptr2 until ptr1 reaches the end of the list
    while ptr1.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.data


# Solution 2: (Using list)
def getNode(head, positionFromTail):
    # Write your code here
    list = []
    ptr = head

    while ptr != None:
        list.append(ptr.data)
        ptr = ptr.next

    return list[len(list) - positionFromTail - 1]


# Solution 3: (Using recursion)
def getNode(head, positionFromTail):
    # Write your code here
    if head == None:
        return 0

    index = getNode(head.next, positionFromTail) + 1

    if index == positionFromTail:
        return head.data

    return index


# Solution 4: (Using stack)
def getNode(head, positionFromTail):
    # Write your code here
    stack = []
    ptr = head

    while ptr != None:
        stack.append(ptr.data)
        ptr = ptr.next

    for i in range(positionFromTail):
        stack.pop()

    return stack.pop()


# Solution 5: (Using dictionary)
def getNode(head, positionFromTail):
    # Write your code here
    dict = {}
    ptr = head
    index = 0

    while ptr != None:
        dict[index] = ptr.data
        ptr = ptr.next
        index += 1

    return dict[index - positionFromTail - 1]


# ********************************************************************************************************

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + "\n")

    fptr.close()
