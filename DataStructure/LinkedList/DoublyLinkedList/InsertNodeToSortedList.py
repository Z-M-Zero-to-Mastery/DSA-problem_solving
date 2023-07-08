# Given a reference to the head of a doubly-linked list and an integer,data , create a new DoublyLinkedListNode object having data value data and insert it at the proper location to maintain the sort.

# Example
# head refers to the list 1 <-> 2 <-> 3 <->NULL
# data=4
#
# The new list is 1 <-> 2 <-> 3 <-> 4 <->NULL

# Return a reference to the head of your adjusted list.

# Sample Input
# 1
# 3
# 1
# 2
# 4
# 5
# 6

# Sample Output
# 1 2 3 4 5 6

# Class for DoublyLinkedListNode
import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# ****************************************************************************************

# Solution 1


def sortedInsert(head, data):
    # Write your code here
    new_node = DoublyLinkedListNode(data)

    if head is None:
        return new_node

    elif head.data >= new_node.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    else:
        rest = sortedInsert(head.next, data)
        head.next = rest
        rest.prev = head
        return head


# Solution 2


def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    # If head is none
    if head is None:
        return node

    # If we want to insert at head postion
    elif head.data >= node.data:
        node.next = head
        head.prev = node
        return node

    else:
        cur = head
        # It will Loop till the last element or postion which we want to insert the node
        while curr.next is not None and curr.next.data < node.data:
            curr = curr.next

        # If the node wants to insert at last position
        if cur.next == None and cur.data < data:
            cur.next = node
            node.prev = cur
        # else case which node wants to insert in between
        else:
            # Insetion for previous postion element
            previous = cur.prev
            previous.next = node
            node.prev = previous
            # Insertion for current postion element
            node.next = cur
            cur.prev = node

        return head


# ****************************************************************************************

# Input
if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, " ", fptr)
        fptr.write("\n")

    fptr.close()
