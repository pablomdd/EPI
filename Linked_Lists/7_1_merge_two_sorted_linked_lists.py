# We iterate trough the lists at the same time
# reusing nodes and placing them in the correct sorte order
# Time: O(n+m)
# Space: O(1) as we reuser nodes

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

def merge_two_sorted_lists(L1, L2):
    # Create a dummy placeholder
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next

        tail = tail.next

# Append remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next