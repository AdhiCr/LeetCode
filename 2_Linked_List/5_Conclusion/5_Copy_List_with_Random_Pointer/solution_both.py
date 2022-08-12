from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hash_map = {}
        new_node = new_node_head = Node(0)
        og_curr = head
        while (og_curr):
            if og_curr in hash_map:
                new_node.next = hash_map[og_curr]
                new_node = new_node.next
                new_node.val = og_curr.val
            else:
                new_node.next = Node(og_curr.val)
                new_node = new_node.next
            hash_map[og_curr] = new_node

            if og_curr.random:
                if og_curr.random not in hash_map:
                    hash_map[og_curr.random] = Node(og_curr.random.val)
                new_node.random = hash_map[og_curr.random]

            og_curr = og_curr.next

        return new_node_head.next