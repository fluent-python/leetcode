# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        counter = 0
        while fast.next:
            fast = fast.next
            if counter == n:
                slow = slow.next
            else :
                counter += 1
        if counter == n :
            rmNode = slow.next
            slow.next = rmNode.next
            rmNode.next = None
        else:
            return head.next
        return head
