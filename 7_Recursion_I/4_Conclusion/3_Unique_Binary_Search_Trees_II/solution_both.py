from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        unique_bsts = {}
        def buildTree(first, last):
            if unique_bsts.get((first, last), []) != []:
                return unique_bsts.get((first, last))

            if first > last:
                return [None]

            trees = []
            for root in range(first, last + 1):
                for left in buildTree(first, root-1):
                    for right in buildTree(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            unique_bsts[(first, last)] = trees
            return trees
        return buildTree(1, n)
