import collections

class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(set)

    def addWord(self, word):
        # add to the bucket with same length
        if word:
            self.word_dict[len(word)].add(word)

    def search(self, word):
        # Edge Case
        if not word:
            return False

        # if '.' not in word given
        if '.' not in word:
            return word in self.word_dict[len(word)]

        # if '.' in word then compare the structure for each word in set with given word
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i]:
                    if ch != '.':
                        break
            else:
                return True
        return False

dummy = WordDictionary()
dummy.addWord("bad")
dummy.addWord("dad")
dummy.addWord("mad")
dummy.addWord("pad")
print(dummy.search("bad"))
print(dummy.search(".ad"))
print(dummy.search("b.."))

dummy = WordDictionary()
dummy.addWord("badge")
dummy.addWord("dad")
dummy.addWord("mad")
dummy.addWord("pad")
print(dummy.search("bad"))
print(dummy.search(".ad"))
print(dummy.search("b.dg."))



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)