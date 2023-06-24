# Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

# Example
# head refers to the list 1 -> 2 -> 3 -> NULL
# Return 3 -> 2 -> 1 -> NULL

# Class definition for Node
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


# The reverse function below.

# ************************************************************************


# Solution 1: Iterative
def reverse(head):
    # Write your code here
    prev = None
    curr = head
    while curr:
        # Store the next node
        next = curr.next
        # Reverse the current node's pointer
        curr.next = prev
        # Move to the next node
        prev = curr
        curr = next
    return prev


# Solution 2: Recursive
def reverse(head):
    # Write your code here
    if not head or not head.next:
        return head
    # Reverse the rest of the list
    rest = reverse(head.next)
    # Put first element at the end
    head.next.next = head
    head.next = None
    # Fix the head pointer
    return rest


# Solution 3: Using stack
def reverse(head):
    # Write your code here
    stack = []
    curr = head

    while curr:
        stack.append(curr)
        curr = curr.next
    head = stack.pop()
    curr = head

    while len(stack) > 0:
        node = stack.pop()
        curr.next = node
        curr = curr.next

    curr.next = None
    return head


# ************************************************************************

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, " ", fptr)
        fptr.write("\n")

    fptr.close()
