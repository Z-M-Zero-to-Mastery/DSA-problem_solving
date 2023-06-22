# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.

# Example
# head refers to the first node in the list 1 -> 2 -> 3
# Delete the node at position 2 and return 1 -> 2
# head = deleteNode(head, 2)

# Sample Input
# 1 -> 2 -> 3 -> NULL, position = 0
# 1 -> NULL , position = 0

# Sample Output
# 2 -> 3 -> NULL

# Explanation
# 0. 0 -> 1 -> 2 -> NULL
# 1. Delete Node at position 0: 1 -> 2 -> NULL
# 2. Delete Node at position 0: 2 -> NULL

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


# The deleteNode function below.

# ************************************************************************************


# Solution 1:
def deleteNode(head, position):
    # This is to check the position of the node to be deleted is the head node
    if position == 0:
        head = head.next

    temp = head
    count = 1

    while temp:
        # This is to check if the position of the node to be deleted is the last node
        if count == position:
            # This will set the next node of the node to be deleted to the next node of the next node of the node to be deleted
            # eg. 1 -> 2 -> 3 -> 4 -> 5
            # position = 2
            # temp = 1
            # temp.next = 2
            # temp.next.next = 3
            # temp.next (1.next) = temp.next.next (1.next.next) = 3
            temp.next = temp.next.next
            break
        count += 1
        temp = temp.next

    return head


# Solution 2:
def deleteNode(head, position):
    if position == 0:
        head = head.next

    else:
        temp = head
        count = 1

        while temp != None and count < position:
            temp = temp.next
            count += 1

        temp.next = temp.next.next

    return head


# ************************************************************************************

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, " ", fptr)
    fptr.write("\n")

    fptr.close()
