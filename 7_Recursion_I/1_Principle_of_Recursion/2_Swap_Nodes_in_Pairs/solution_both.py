from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp_node = ListNode(next=head.next)
            head.next = self.swapPairs(head=temp_node.next.next)
            temp_node.next.next = head
            return temp_node.next
        else:
            return head
