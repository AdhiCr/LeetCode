from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head, l1_prev = None, ListNode()

        print(f"{list1}\n{list2}")
        while (list1 and list2):
            if l1_head is None:
                l1_head = list1 if list1.val < list2.val else list2

            if list1.val >= list2.val:
                tmp = list2.next
                l1_prev.next = list2
                l1_prev = list2
                list2.next = list1
                list2 = tmp

            else:
                l1_prev = list1
                list1 = list1.next

        if list2:
            if not l1_head:
                l1_head = list2
            else:
                l1_prev.next = list2
        elif not l1_head:
            l1_head = list1

        return l1_head





