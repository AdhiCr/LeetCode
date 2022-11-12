from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif list1.val <= list2.val:
            head = ListNode(list1.val)
            head.next = self.mergeTwoLists(list1.next, list2)
            return head
        elif list1.val > list2.val:
            head = ListNode(list2.val)
            head.next = self.mergeTwoLists(list1, list2.next)
            return head






