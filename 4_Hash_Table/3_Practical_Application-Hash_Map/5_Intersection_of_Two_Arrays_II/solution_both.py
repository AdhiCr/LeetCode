from typing import List
from collections import Counter


class Solution:
    def count_in_other_list(self, ip_list: List[int]) -> List[int]:
        output = []
        for n in ip_list:
            if n in self.dict_map:
                output.append(n)
                self.dict_map[n] -= 1
                if not self.dict_map[n]: del self.dict_map[n]
        return output


    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.dict_map = Counter(nums1) if len(nums1) > len(nums2) else Counter(nums2)
        if len(nums1) > len(nums2):
            return self.count_in_other_list(nums2)
        else:
            return self.count_in_other_list(nums1)