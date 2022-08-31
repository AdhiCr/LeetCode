from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False

dummy = Solution()
print(dummy.containsNearbyDuplicate([1,2,3,1], 3))  # True
print(dummy.containsNearbyDuplicate([1,0,1,1], 1))  # True
print(dummy.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # False
print(dummy.containsNearbyDuplicate([4,1,2,3,1,5], 3))  # True
print(dummy.containsNearbyDuplicate([99,99], 2))  # True