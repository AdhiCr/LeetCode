from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 or l2:
            if l1 == l2:
                return l1
            l1 = headB if not l1 else l1.next
            l2 = headA if not l2 else l2.next