class TrieNode:
    def __init__(self, sum_val=0):
        self.children = dict()
        self.sum_val = sum_val


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        cur.sum_val += val
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode(val)
            elif c in cur.children:
                cur.children[c].sum_val += val
            cur = cur.children[c]

    def sum(self, prefix: str) -> int:
        cur = self.root
        sum_val = 0
        for c in prefix:
            if c in cur.children:
                sum_val = cur.children[c].sum_val
                cur = cur.children[c]
            else:
                sum_val = 0
        return sum_val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

dummy = MapSum()
print(dummy.insert("apple", 3))
print(dummy.sum("ap"))
print(dummy.insert("app", 2))
print(dummy.sum("ap"))