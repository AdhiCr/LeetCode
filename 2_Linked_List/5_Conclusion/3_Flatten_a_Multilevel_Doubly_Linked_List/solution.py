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
        curr = head

        while (curr):
            if curr.child:
                last_of_child = self.flatten_child(curr.child)

                last_of_child.next = curr.next
                curr.child.prev = curr

                curr.next = curr.child
                curr.child = None

                if last_of_child.next:
                    curr = last_of_child.next
                    curr.prev = last_of_child
            elif curr.next:
                curr = curr.next
            else:
                break
        return head

    def flatten_child(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while (curr):
            if curr.child:
                last_of_child = self.flatten_child(curr.child)

                last_of_child.next = curr.next
                curr.child.prev = curr

                curr.next = curr.child
                curr.child = None

                if last_of_child.next:
                    curr = last_of_child.next
                    curr.prev = last_of_child
            elif curr.next:
                curr = curr.next
            else:
                break
        return curr
