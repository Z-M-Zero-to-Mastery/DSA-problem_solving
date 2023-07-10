# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.

# Return a reference to the head node of the reversed list.

# Sample Input
# 1 <-> 2 <-> 3 <-> NULL


# Sample Output
# 3 <-> 2 <-> 1 <-> NULL


# Solution 1
def reverse(head):
    # This loop will reverse the next and prev pointers of each node till the last node
    while head.next != None:
        head.next, head.prev, head = head.prev, head.next, head.next

    # This statement will reverse the next and prev pointers of the last node
    head.next, head.prev = head.prev, None

    return head


# Solution 2


def reverse(head):
    if head is None:
        return None
    else:
        current = head
        prev = None
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next

        head = prev
        return head


# Solution 3


def reverse(head):
    if head == None:
        return

    temp = head

    # This loop will take the pointer to the last node
    while temp.next != None:
        temp = temp.next

    # This statement will make the last node as the head node .
    head = temp
    cur = head
    previous = cur.prev
    nxt = cur.next

    # This statement will reverse the next and prev pointers of the last node
    cur.next = previous
    cur.prev = nxt

    # This loop will reverse the next and prev pointers of each node till the first node
    while cur.next != None:
        # This statement will move the pointer to the previous node of the current node
        # Same process as above
        cur = cur.next
        previous = cur.prev
        nxt = cur.next

        cur.next = previous
        cur.prev = nxt

    return head
