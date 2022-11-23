# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int, bad_version: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if mid == bad_version:
                right = mid
            else:
                left = mid + 1

        if left == bad_version:
            return left


dummy = Solution()
print(dummy.firstBadVersion(5,4))
print(dummy.firstBadVersion(1,1))
print(dummy.firstBadVersion(9,9))