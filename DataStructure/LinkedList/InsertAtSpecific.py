# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its data attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

# Example

# head refers to the first node in the list 1->2->3
# data=4
# position=2

# Insert a node at position 2 with data=4. The new list is 1->2->4->3

# Sample Input

# 3
# 16
# 13
# 7
# 1
# 2
# Sample Output

# 16 13 1 7
# Explanation

# The initial linked list is 16 13 7. We have to insert 1 at the position 2 which currently has 7 in it. The updated linked list will be 16 13 1 7

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


# The insertNodeAtPosition function below.
# *************************************************************************************

# Solution 1: Iterative


def insertNodeAtPosition(head, data, position):
    # Write your code here
    # Create a new node with the given data
    new_node = SinglyLinkedListNode(data)

    # If the head is null, then make the new node as head
    if head == None:
        head = new_node
    # Else, traverse the list till the position and insert the new node
    else:
        # Initialize the temp node as head
        temp = head

        # Traverse the list till the position
        for i in range(position - 1):
            temp = temp.next
        # Insert the new node at the position
        new_node.next = temp.next
        temp.next = new_node

    # Return the head
    return head


# Solution 2:


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)

    if head == None:
        return node

    temp = head
    count = 1

    while temp:
        if position == count:
            node.next = temp.next
            temp.next = node

            break

        temp = temp.next
        count += 1

    return head


# *************************************************************************************

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, " ", fptr)
    fptr.write("\n")

    fptr.close()
