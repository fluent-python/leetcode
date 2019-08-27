# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        elif head.next == None:
            return head
        odd_head = head
        even_head = head.next
        # odd
        odd = odd_head
        even = even_head
        while True:
            odd.next = even.next 
            
            if odd.next == None:
                odd.next = even_head
                break

            odd = odd.next
            even.next = odd.next

            if even.next == None:
                odd.next = even_head
                break
            even = even.next
            
        return head
        
