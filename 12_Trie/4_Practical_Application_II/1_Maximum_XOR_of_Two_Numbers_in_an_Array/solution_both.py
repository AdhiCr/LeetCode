from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        bit_count = max(nums).bit_length()
        best_possible = (1 << bit_count) - 1
        # available = set()
        # for i in range(n):
        #     available.add(nums[i])
        available = set(nums)

        for left in range(n):
            bst = best_possible - left
            for i in range(n):
                if (bst ^ nums[i]) in available:
                    return bst

        for i in range(n):
            for j in range(i + 1, n):
                cur = nums[i] ^ nums[j]
                best = max(best, cur)
            if best == best_possible:
                break
        return best


dummy = Solution()
print(dummy.findMaximumXOR([3,10,5,25,2,8]))

dummy = Solution()
print(dummy.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
