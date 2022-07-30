from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while (curr):
            tmp = curr.next
            if tmp and tmp.val == val:
                curr.next = tmp.next
            else:
                curr = tmp

        return head.next if (head and head.val == val) else head
