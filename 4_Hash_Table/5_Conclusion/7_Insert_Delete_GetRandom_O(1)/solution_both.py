from random import randint

class RandomizedSet:
    def __init__(self):
        self.set_list = list()

    def insert(self, val: int) -> bool:
        if val not in self.set_list:
            self.set_list.append(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.set_list:
            self.set_list.remove(val)
            return True
        else:
            False

    def getRandom(self) -> int:
        return self.set_list[randint(0, len(self.set_list) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()