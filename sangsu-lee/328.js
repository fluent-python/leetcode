/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 * @param {ListNode} head
 * @return {ListNode}
 */

function ListNode(val) {
    this.val = val;
    this.next = null;
}

let oddEvenList = function(head) {
    if (head == null || head.next == null) return head;
    let oddHead = head;
    let evenHead = head.next;
    
    let cur1 = head;
    let cur2 = head.next;
    let oddTail = cur1;
    while (true) {
        if (cur2.next == null) {
            break;
        }
        if (cur2.next.next == null) {
            cur1.next = cur2.next;
            cur2.next = null;
            oddTail = cur1.next;
            break;
        }
        cur1.next = cur2.next;
        cur2.next = cur2.next.next;
        oddTail = cur1.next;
        cur1 = cur1.next;
        cur2 = cur2.next;
    }
    oddTail.next = evenHead;
    return head;
};

let head = new ListNode(1);
let cur = head;
let nodeLen = 2;

for (let i = 2; i < nodeLen + 1; i++) {
    cur.next = new ListNode(i);
    cur = cur.next;
}


let printNodes = function(head, maxcnt) {
    cur = head;
    while (cur && maxcnt--) {
        console.log(cur.val)
        cur = cur.next;
    }
}
//printNodes(head);
oddEvenList(head);
printNodes(head, 5);

