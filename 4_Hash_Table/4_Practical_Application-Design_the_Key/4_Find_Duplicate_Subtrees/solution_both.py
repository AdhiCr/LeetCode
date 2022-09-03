from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deapthFirstSearch(self, node: Optional[TreeNode]) -> str:
        if not node:
            return ""
        path_map = (f"{node.val} {self.deapthFirstSearch(node.left)} {self.deapthFirstSearch(node.right)}")
        self.tree_mappings[path_map] += 1
        if self.tree_mappings[path_map] == 2:
            self.duplicates_sub_trees.append(node)
        return path_map

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.duplicates_sub_trees = []
        self.tree_mappings = defaultdict(lambda: 0)
        self.deapthFirstSearch(root)
        return self.duplicates_sub_trees