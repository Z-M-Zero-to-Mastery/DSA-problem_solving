# This is an to practice traversing a linked list. Given a pointer to the head node of a linked list, print each node's data element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.

# Sample Input

#  2
#  16
#  13
# Sample Output

#  16
#  13
# Explanation

# There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the printLinkedList function should print 16 and 13 each in a new line.

# Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

# printLinkedList has the following parameters:

# SinglyLinkedListNode pointer head: a reference to the head of the list
# Prints
# The  value of each node in the linked list.

# bin/python3
# Class definition for SinglyLinkedListNode
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


def printLinkedList(head):
    if head:
        print(head.data)
        printLinkedList(head.next)


# Input

print("Enter the number of elements in the linked list")
n = int(input())

printLinkedList(n)
