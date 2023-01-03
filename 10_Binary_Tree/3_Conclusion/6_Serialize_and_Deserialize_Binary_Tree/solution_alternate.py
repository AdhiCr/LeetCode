from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        result = []
        queue = deque([root])
        while len(queue) != 0:
            node = queue.popleft()
            if node != None:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        while result[-1] == "null":
            result.pop()

        return ",".join(result)

    def deserialize(self, data):
        tmp = TreeNode(data) if data else None
        # return TreeNode(data) if data else None
        return tmp

dummy = Codec()
tree = dummy.deserialize("1,2,3,null,null,4,5")
tmp = 5

# ['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X']
# ['X']
# ['4', '-7', 'X', 'X', '-3', '-9', '9', '6', '0', 'X', '-1', 'X', 'X', '6', '-4', 'X', 'X', 'X', 'X', '-7', '-6', '5', 'X', 'X', 'X', '-6', '9', '-2', 'X', 'X', 'X', 'X', '-3', '-4', 'X', 'X', 'X']
