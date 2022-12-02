class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return num

        start = 1
        end = num//2

        while start<=end:
            mid = (start + end)//2
            tmp_sq = mid * mid
            if tmp_sq == num:
                return True
            elif tmp_sq < num:
                start = mid + 1
            else:
                end = mid - 1

        return False

dummy = Solution()
for i in range(1, 101):
    print(f"{i}\t{dummy.isPerfectSquare(i)}")