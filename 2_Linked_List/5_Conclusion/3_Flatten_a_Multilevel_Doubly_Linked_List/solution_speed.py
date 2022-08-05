from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        _ = self.flatten_child(head)
        return head

    def flatten_child(self, curr: 'Optional[Node]') -> 'Optional[Node]':
        last = None
        while (curr):
            curr_next = curr.next
            if curr.child:
                last_of_child = self.flatten_child(curr.child)
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None

                if curr_next:
                    last_of_child.next = curr_next
                    curr_next.prev = last_of_child
                last = last_of_child
            else:
                last = curr
            curr = curr_next
        return last
