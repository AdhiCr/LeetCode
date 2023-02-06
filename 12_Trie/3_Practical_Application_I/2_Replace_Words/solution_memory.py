from typing import List


class Solution:
    def findPrefix(self, word, dictSet):
        for pre in range(1, len(word)):
            if word[:pre] in dictSet:
                return word[:pre]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        return " ".join(self.findPrefix(w, set(dictionary)) for w in sentence.split())

dummy = Solution()
print(dummy.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
dummy = Solution()
print(dummy.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
dummy = Solution()
print(dummy.replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))


