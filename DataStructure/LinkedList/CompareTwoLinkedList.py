# You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return 1. Otherwise, return 0.

# Example
# list1 = 1 -> 2 -> 3 -> NULL
# list2 = 1 -> 2 -> 3 -> NULL
# The two lists have equal data attributes for the nodes and are the same length. Return 1.

# list1 = 1 -> 2 -> 3 -> NULL
# list2 = 1 -> 2 -> NULL
# list1 has one more node than list2 and the nodes are mismatched (data attribute of node two is different). Return 0.

# Class definition for Node of Linked List
import os
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


# The Compare function is below

# ************************************************************************************


def CompareLists(head1, head2):
    if head1 == None or head2 == None:
        return 0

    temp1 = head1
    temp2 = head2

    while temp1 != None and temp2 != None:
        if temp1.data != temp2.data:
            return 0

        if (temp1.next == None and temp2.next) or (temp2.next == None and temp1.next):
            return 0

        temp1 = temp1.next
        temp2 = temp2.next

    return 1


# Solution 2


def CompareLists(head1, head2):
    if head1 == None or head2 == None:
        return 0

    temp1 = head1
    temp2 = head2

    while temp1 != None and temp2 != None:
        if temp1.data != temp2.data:
            return 0

        temp1 = temp1.next
        temp2 = temp2.next

    if temp1 == None and temp2 == None:
        return 1
    else:
        return 0


# Solution 3: Recursive


def CompareLists(head1, head2):
    if head1 == None or head2 == None:
        return 0

    if head1.data != head2.data:
        return 0

    if head1.next == None and head2.next == None:
        return 1

    return CompareLists(head1.next, head2.next)


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

        result = CompareLists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + "\n")

    fptr.close()
