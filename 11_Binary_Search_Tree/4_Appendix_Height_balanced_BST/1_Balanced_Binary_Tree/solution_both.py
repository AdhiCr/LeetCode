from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, node, last, depths = [], root, None, {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[node] = max(left, right) + 1
                    last = node
                    node = None
                else:
                    node = node.right

        return True


dummy = Solution()
print(dummy.isBalanced([3,9,20,null,null,15,7]))
print(dummy.isBalanced([1,2,2,3,3,null,null,4,4]))
print(dummy.isBalanced([]))
