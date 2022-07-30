from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_pointer = slow_pointer = head
        rev = None
        while fast_pointer and fast_pointer.next:
            rev, rev.next, slow_pointer, fast_pointer = slow_pointer, rev, slow_pointer.next, fast_pointer.next.next

        if fast_pointer:
            slow_pointer = slow_pointer.next
        while rev and rev.val == slow_pointer.val:
            rev, slow_pointer = rev.next, slow_pointer.next
        return not rev