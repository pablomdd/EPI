# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = sublist_head = ListNode(0, head)
        
        for _ in range(1, m):
            sublist_head = sublist_head.next
            
        sublist_iter = sublist_head.next
        
        for _ in range(n - m):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp
            
        return dummy_head.next