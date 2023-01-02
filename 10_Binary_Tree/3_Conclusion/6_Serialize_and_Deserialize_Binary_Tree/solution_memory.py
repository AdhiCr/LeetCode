# "12XX34XX5XX"

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class codec:
    def serialize(self, root):
        if not root:
            return "X"

        return str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):

        def construct_tree(node_val):
            if node_val[0] != "X":
                node = TreeNode(int(node_val.pop(0)))

                if len(node_val) > 0 and node_val[0] != "X":
                    node.left, node_val = construct_tree(node_val)
                else:
                    node_val.pop(0)

                if len(node_val) > 0 and node_val[0] != "X":
                    node.right, node_val = construct_tree(node_val)
                else:
                    node_val.pop(0)
            else:
                return None, node_val

            return node, node_val

        return construct_tree(data)[0]

dummy = codec()
tree = dummy.deserialize(['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X'])
tmp = 5

# ['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X']
# ['X']
# ['4', '-7', 'X', 'X', '-3', '-9', '9', '6', '0', 'X', '-1', 'X', 'X', '6', '-4', 'X', 'X', 'X', 'X', '-7', '-6', '5', 'X', 'X', 'X', '-6', '9', '-2', 'X', 'X', 'X', 'X', '-3', '-4', 'X', 'X', 'X']
