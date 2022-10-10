from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode(next=head)
        p_1, p_2 = head, head.next

        while p_2:
            if p_2.val >= p_1.val:
                p_1, p_2 = p_2, p_2.next
                continue

            dum_p = dummy_head
            while p_2.val > dum_p.next.val:
                dum_p = dum_p.next

            p_1.next = p_2.next
            p_2.next = dum_p.next
            dum_p.next = p_2
            p_2 = p_1.next

        return dummy_head.next

