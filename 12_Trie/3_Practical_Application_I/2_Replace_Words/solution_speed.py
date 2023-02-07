from typing import List


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic = {w: len(w) for w in dictionary}
        mini, maxi = min(dic.values()), max(dic.values())
        split_sen = sentence.split()
        ret_sentence = []
        for word in split_sen:
            for k in range(mini, min(maxi, len(word))+1):
                if word[:k] in dic:
                    word = word[:k]
                    break 
            ret_sentence.append(word)
        return " ".join(ret_sentence)

dummy = Solution()
print(dummy.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
dummy = Solution()
print(dummy.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
dummy = Solution()
print(dummy.replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))


