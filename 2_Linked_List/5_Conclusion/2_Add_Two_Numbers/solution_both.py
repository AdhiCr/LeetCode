from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_list_head = ListNode()
        sum_list = sum_list_head
        while (l1 or l2):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            sum_value = l1_value + l2_value + carry
            sum_list.next = ListNode(sum_value % 10)
            sum_list = sum_list.next
            carry = sum_value // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            sum_list.next = ListNode(carry)

        return sum_list_head.next



