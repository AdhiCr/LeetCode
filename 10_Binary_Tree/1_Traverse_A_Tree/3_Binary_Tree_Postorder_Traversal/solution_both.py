from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_level_order(nodes_list):
            print(nodes_list)
            if not nodes_list:
                return []
            children = []
            values = []
            for node in nodes_list:
                if root.left:
                    children.append(root.left)
                    values.append(root.left.val)
                if root.right:
                    children.append(root.right)
                    values.append(root.right.val)
            print(children)
            print(values)
            values.append(get_level_order(children))
            print(values)
            print("\n\n")
            return values
        vals = get_level_order([root])
        return vals