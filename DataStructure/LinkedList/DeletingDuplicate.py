# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.

# Example
# head refers to the first node in the list 1 -> 2 -> 2 -> 3
# Delete duplicate nodes 1 -> 2 -> 3 -> NULL

# Sample Input
# 6
# 1
# 2
# 2
# 3
# 3
# 4

# Sample Output
# 1 2 3 4

# Explanation
# 1, 2, and 3 are the duplicate nodes, so they are deleted and the remaining nodes are printed in a single line.


# Solution 1: Using Dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeDuplicates(head):
    # Write your code here
    if head is None:
        return head
    else:
        current = head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head


# Solution 2: Using Set
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeDuplicates(head):
    # Write your code here
    if head is None:
        return head
    else:
        current = head
        s = set()
        s.add(current.data)
        while current.next is not None:
            if current.next.data in s:
                current.next = current.next.next
            else:
                s.add(current.next.data)
                current = current.next
        return head


# Solution 3: Using Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeDuplicates(head):
    # Write your code here
    if head is None:
        return head
    elif head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
            removeDuplicates(head)
        else:
            removeDuplicates(head.next)
    return head


# Solution 4: Using Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def removeDuplicates(head):
    # Write your code here
    if head is None:
        return head
    else:
        current = head
        stack = []
        stack.append(current.data)
        while current.next is not None:
            if current.next.data in stack:
                current.next = current.next.next
            else:
                stack.append(current.next.data)
                current = current.next
        return head


# Solution 5: Using Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def removeDuplicates(head):
    # Write your code here
    if head is None:
        return head
    else:
        current = head
        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
