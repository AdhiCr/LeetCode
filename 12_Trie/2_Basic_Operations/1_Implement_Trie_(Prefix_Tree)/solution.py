class Trie:

    def __init__(self):
        self.trie = self.trie_node()

    def insert(self, word: str) -> None:
        tmp = self.trie
        for char in word:
            if not char in tmp["children"]:
                tmp[char] = self.trie_node()
            tmp = tmp[char]
        tmp["end_char"] = True

    def search(self, word: str) -> bool:
        tmp =self.trie
        for char in word:
            if not char in tmp["children"]:
                return False
            tmp = tmp[char]
        return tmp["end_char"]


    def startsWith(self, prefix: str) -> bool:
        tmp = self.trie["root"]
        for char in prefix:
            if not char in tmp["children"]:
                return False
            tmp = tmp[char]
        return True

    def trie_node(self, root=False, end_char=False):
        return {
            "root": root,
            "children": {},
            "end_char": end_char
        }

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

dummy = Trie()
print(dummy.insert("apple"))
print(dummy.search("apple"))
print(dummy.search("app"))
print(dummy.startsWith("app"))
print(dummy.insert("app"))
print(dummy.search("app"))