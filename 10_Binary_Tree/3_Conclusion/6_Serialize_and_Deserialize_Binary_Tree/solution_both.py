# "12XX34XX5XX"

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def serialiser(node):
            if node:
                vals.append(str(node.val))
                serialiser(node.left)
                serialiser(node.right)
            else:
                vals.append('#')
        vals = []
        serialiser(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def deserialiser():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deserialiser()
            node.right = deserialiser()
            return node
        vals = iter(data.split())
        return deserialiser()

dummy = Codec()
tree = dummy.deserialize(['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X'])
tmp = 5

# ['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X']
# ['X']
# ['4', '-7', 'X', 'X', '-3', '-9', '9', '6', '0', 'X', '-1', 'X', 'X', '6', '-4', 'X', 'X', 'X', 'X', '-7', '-6', '5', 'X', 'X', 'X', '-6', '9', '-2', 'X', 'X', 'X', 'X', '-3', '-4', 'X', 'X', 'X']
