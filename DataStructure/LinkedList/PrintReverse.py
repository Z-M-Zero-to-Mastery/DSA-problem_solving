# Given a pointer to the head of a singly-linked list, print each data value from the reversed list. If the given list is empty, do not print anything.
# Example:
# head refers to the linked list with data values 1 -> 2 -> 3 -> NULL
# Print the following:
# 3
# 2
# 1
# NULL

# Sample Input:
# This example uses the following two linked lists:
# NULL
# 1->2->3->NULL
# and  are the two head nodes passed as arguments to printLinkedList.

# Sample Output:
# 3
# 2
# 1

# Explanation:
# First list is empty. Second list contains 3 nodes, so we print each element in reverse order.

# Class definition for a Node of a Singly Linked List
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


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end="")

        node = node.next

        if node:
            print(sep, end="")


# The reversePrint function below.
# **********************************************************************


def reversePrint(head):
    # Write your code here
    if head is None:
        return
    else:
        reversePrint(head.next)
        print(head.data)


# **********************************************************************

if __name__ == "__main__":
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)
