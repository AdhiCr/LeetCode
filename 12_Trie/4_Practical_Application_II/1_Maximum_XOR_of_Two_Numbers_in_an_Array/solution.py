from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.flip = {
            "0": "1",
            "1": "0"
        }
        self.max_pow = 0

    def insert_number(self, number):
        bin_eql = bin(number)[2:].zfill(self.max_pow)
        node = self.root
        for bit in bin_eql:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def get_max_xor(self, number):
        bin_eql = bin(number)[2:].zfill(self.max_pow)
        node = self.root
        max_xor = ""

        for bit in bin_eql:
            if self.flip[bit] in node.children:
                max_xor += "1"
                node = node.children[self.flip[bit]]
            else:
                max_xor += "0"
                node = node.children[bit]

        return int(max_xor, 2)

    def findMaximumXOR(self, nums: List[int]) -> int:
        self.max_pow = len(bin(max(nums))[2:])
        for num in nums:
            self.insert_number(num)

        ret_max = self.get_max_xor(nums[0])
        for num in nums[1:]:
            ret_max = max(ret_max, self.get_max_xor(num))

        return ret_max

dummy = Solution()
print(dummy.findMaximumXOR([3,10,5,25,2,8]))

dummy = Solution()
print(dummy.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
