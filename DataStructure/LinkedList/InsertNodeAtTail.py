# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

# Sample Input

# 5
# 141
# 302
# 164
# 530
# 474
# Sample Output

# 141
# 302
# 164
# 530
# 474
# Explanation

# First the linked list is NULL. After inserting 141, the list is 141 -> NULL.
# After inserting 302, the list is 141 -> 302 -> NULL.
# After inserting 164, the list is 141 -> 302 -> 164 -> NULL.
# After inserting 530, the list is 141 -> 302 -> 164 -> 530 -> NULL.
# After inserting 474, the list is 141 -> 302 -> 164 -> 530 -> 474 -> NULL, which is the final list.

# Class for a node of a linked list
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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# The insertNodeAtTail function below.
# *************************************************************************************


def insertNodeAtTail(head, data):
    # Write your code here.
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head


# *************************************************************************************

# Input

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, "\n", fptr)
    fptr.write("\n")

    fptr.close()
