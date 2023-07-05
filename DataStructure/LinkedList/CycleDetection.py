# A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

# Example
# head refers to the list of nodes 1 -> 2 -> 3 -> NULL
# The numbers shown are the node numbers, not their data values. There is no cycle in this list so return 0.

# head refers to the list of nodes 1 -> 2 -> 3 -> 1 -> NULL
# There is a cycle where node 3 points back to node 1, so return 1.

# Returns 1 if there is a cycle else returns 0.

# Solution 1: using two pointers


def has_cycle(head):
    if head is None:
        return 0
    slow = head
    fast = head.next

    # if there is a cycle, the fast pointer will eventually catch up with the slow pointer
    # if there is no cycle, the fast pointer will reach the end of the list
    # eg : 1 -> 2 -> 3 -> 1 -> NULL
    # slow = 1, fast = 2
    # slow = 2, fast = 1 (After 1st iteration)
    # slow = 3, fast = 2 (After 2nd iteration)
    # slow = 1, fast = 1 (After 3rd iteration)
    while slow != fast:
        # It checks if the fast pointer or the next node of the fast pointer is null
        # if it is null, it means that there is no cycle

        if fast is None or fast.next is None:
            return 0
        # slow pointer moves one node at a time
        # fast pointer moves two nodes at a time
        # eg : 1 -> 2 -> 3 -> 1 -> NULL
        slow = slow.next
        fast = fast.next.next
    return 1


# Solution 2: using a dictionary


def has_cycle(head):
    dic = {}
    while head:
        if head in dic:
            return 1

        # if the node is not in the dictionary, add it to the dictionary
        # if the node is already in the dictionary, it means that there is a cycle
        # eg : 1 -> 2 -> 3 -> 1 -> NULL
        # dic = {1:1}
        # dic = {1:1, 2:1}
        # dic = {1:1, 2:1, 3:1}
        # dic = {1:1, 2:1, 3:1} (After 4th iteration)
        dic[head] = 1
        head = head.next

    return 0
