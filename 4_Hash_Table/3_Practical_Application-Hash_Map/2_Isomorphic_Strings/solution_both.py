class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = dict()

        for char_a, char_b in zip(s, t):
            if char_a not in char_dict:
                char_dict[char_a] = char_b
            elif char_dict[char_a] == char_b:
                continue
            else:
                return False

            if len(char_dict.values()) != len(set(char_dict.values())):
                return False
        return True


dummy =Solution()
print(dummy.isIsomorphic(s = "egg", t = "add"))
print(dummy.isIsomorphic(s = "foo", t = "bar"))
print(dummy.isIsomorphic(s = "paper", t = "title"))
print(dummy.isIsomorphic(s = "badc", t = "baba"))