from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None:
            return head
        else:
            curr = head
            list_len = 1
            while(curr.next):
                list_len += 1
                curr = curr.next
            curr.next = head
            for i in range(list_len - (k % list_len)):
                curr = curr.next
            head = curr.next
            curr.next = None
            return head