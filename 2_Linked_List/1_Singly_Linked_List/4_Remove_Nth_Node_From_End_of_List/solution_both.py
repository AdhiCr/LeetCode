from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trailing_pointer = leading_pointer = head
        for _ in range(n):
            leading_pointer = leading_pointer.next

        if not leading_pointer:
            return head.next

        while (leading_pointer.next):
            leading_pointer = leading_pointer.next
            trailing_pointer = trailing_pointer.next

        trailing_pointer.next = trailing_pointer.next.next

        return head
