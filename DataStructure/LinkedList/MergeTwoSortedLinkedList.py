# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

# Example
# list1 = 1 -> 2 -> 3 -> NULL
# list2 = 1 -> 2 -> 3 -> NULL

# Merge the two lists together into a single sorted list:
# 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> NULL

# Class definition for Node of Linked List
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


# The MergeLists function is below

# ************************************************************************************


def MergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None

    if head1 == None:
        return head2

    if head2 == None:
        return head1

    temp1 = head1
    temp2 = head2
    head3 = SinglyLinkedList()
    temp3 = head3

    while temp1 != None and temp2 != None:
        if temp1.data <= temp2.data:
            temp3.insert_node(temp1.data)
            temp1 = temp1.next
        else:
            temp3.insert_node(temp2.data)
            temp2 = temp2.next

    while temp1 != None:
        temp3.insert_node(temp1.data)
        temp1 = temp1.next

    while temp2 != None:
        temp3.insert_node(temp2.data)
        temp2 = temp2.next

    return head3.head


# Solution 2: Recursive Solution


def MergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None

    if head1 == None:
        return head2

    if head2 == None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = MergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = MergeLists(head1, head2.next)

    return temp


# ************************************************************************************


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = MergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, " ", fptr)
        fptr.write("\n")

    fptr.close()
