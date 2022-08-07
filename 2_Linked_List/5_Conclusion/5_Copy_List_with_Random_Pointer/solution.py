from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hash_map = {None: None}
        og_curr = head
        while (og_curr):
            hash_map[og_curr] = Node(x=og_curr.val)
            og_curr = og_curr.next

        og_curr = head
        while (og_curr.next):
            hash_map[og_curr].next = hash_map[og_curr.next]
            hash_map[og_curr].random = hash_map[og_curr.random]
            og_curr = og_curr.next

        return hash_map[head]