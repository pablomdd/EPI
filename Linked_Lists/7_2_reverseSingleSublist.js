/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    if(head == null){
        return null;
    }
    
    let prev = head;
    
    for(let i = 1; i <= m-1; i++){
// look for prev node
        prev = prev.next;
    }
    
    let curr = prev.next;
    let anchor = prev, tail = curr;
    
//     reverse sublist
    for(let i = 1; i < n-m; i++){
        let tempNode = curr.next;
// point backward
        curr.next = prev;
// move on
        prev.next = curr;
        curr = tempNode
    }
    
    if(anchor != null){
        anchor.next = prev;
    } else {
        head = prev;
    }
    
    tail.next = curr;
    return head;
};


/*
Sigle Pass:
- get the anchor node
- reverse the sublist with a dummy head
- attach back de sublist
1->2->3->4-> null
dummyHead: null<-2<-3<-

1->3....2->4

Time: O(n)
Space: O(1)

*/