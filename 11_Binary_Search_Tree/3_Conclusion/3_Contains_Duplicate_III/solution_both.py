from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dct = {}
        for i, num in enumerate(nums):
            key = num // (valueDiff + 1)
            if key in dct:
                return True
            if key-1 in dct:
                if abs(dct[key-1] - num) <= valueDiff:
                    return True
            if key + 1 in dct:
                if abs(dct[key+1] - num) <= valueDiff:
                    return True
            dct[key] = num
            if i >= indexDiff:
                del_key = nums[i-indexDiff] // (valueDiff + 1)
                del dct[del_key]
        return False

dummy = Solution()
print(dummy.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
print(dummy.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))


