# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = []
        while head is not None:
            num_list.append(head.val)
            head = head.next

        left, right = 0, len(num_list) - 1
        while left < right:
            if num_list[left] == num_list[right]:
                left, right = left+1, right-1
            else:
                return False
        return True

