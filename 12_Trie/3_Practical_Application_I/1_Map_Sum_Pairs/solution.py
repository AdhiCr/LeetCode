# Source: https://github.com/black-shadows/LeetCode-Topicwise-Solutions/blob/master/Python/map-sum-pairs.py

import collections


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__root = _trie()


    def insert(self, key, val):
        # Time: O(n)
        curr = self.__root
        for c in key:
            curr = curr[c]
        delta = val
        if "_end" in curr:
            delta -= curr["_end"]

        curr = self.__root
        for c in key:
            curr = curr[c]
            if "_count" in curr:
                curr["_count"] += delta
            else:
                curr["_count"] = delta
        curr["_end"] = val


    def sum(self, prefix):
        # Time: O(n)
        curr = self.__root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr["_count"]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


dummy = MapSum()
print(dummy.insert("apple", 3),
      dummy.sum("ap"),
      dummy.insert("app", 2),
      dummy.sum("ap"))
print("\n")

dummy = MapSum()
print(dummy.insert("a", 3),
      dummy.sum("ap"),
      dummy.insert("b", 2),
      dummy.sum("a"))
print("\n")

dummy = MapSum()
print(dummy.insert("apple", 3),
      dummy.sum("ap"),
      dummy.insert("app", 2),
      dummy.insert("apple", 2),
      dummy.sum("ap"))
print("\n")
"""
["MapSum","insert","sum","insert","sum"]
[[],["apple",3],["ap"],["app",2],["ap"]] -> [null,null,3,null,5]
["MapSum","insert","sum","insert","sum"]
[[],["a",3],["ap"],["b",2],["a"]] -> [null,null,0,null,3]
["MapSum","insert","sum","insert","insert","sum"]
[[],["apple",3],["ap"],["app",2],["apple",2],["ap"]] -> [null,null,3,null,null,4]
["MapSum","insert","sum","insert","sum","insert","insert","sum"]
[[],["apple",3],["ap"],["app",2],["ap"],["apple",5],["apple",1],["apple"]] -> [null,null,3,null,5,null,null,1]
"""