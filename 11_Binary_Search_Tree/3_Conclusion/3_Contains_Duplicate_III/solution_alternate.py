from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dct = {}
        for i, num in enumerate(nums):
            key = num // (valueDiff + 1)
            if key in dct and abs(i - dct[key][0]) <= indexDiff:
                return True
            if key-1 in dct:
                idx, val = dct[key-1]
                if abs(i-idx) <= indexDiff and abs(val-num) <= valueDiff:
                    return True
            if key+1 in dct:
                idx, val = dct[key+1]
                if abs(i-idx) <= indexDiff and abs(val-num) <= valueDiff:
                    return True
            dct[key] = [i, num]
        return False

dummy = Solution()
print(dummy.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
print(dummy.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))


