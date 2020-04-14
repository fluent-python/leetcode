# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        i = 0
        while fast.next:
            i += 1
            fast = fast.next
            if i % 2 != 0:
                slow = slow.next
        return slow

