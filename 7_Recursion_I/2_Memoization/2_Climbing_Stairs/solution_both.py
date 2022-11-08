class Solution:
    def __init__(self):
        self.ways_to_reach_from_n = {
            1: 1,
            2: 2
        }

    def climbStairs(self, n: int) -> int:
        if self.ways_to_reach_from_n.get(n, False):
            return self.ways_to_reach_from_n[n]
        else:
            self.ways_to_reach_from_n[n] = 0

        if n - 2 == 0:
            self.ways_to_reach_from_n[n] += 1
        elif n > 2:
            self.ways_to_reach_from_n[n] += self.climbStairs(n - 2)

        if n - 1 == 0:
            self.ways_to_reach_from_n[n] += 1
        elif n > 1:
            self.ways_to_reach_from_n[n] += self.climbStairs(n - 1)

        return self.ways_to_reach_from_n[n]



dummy = Solution()
print(dummy.climbStairs(2))
print(dummy.climbStairs(3))
print(dummy.climbStairs(10))
print(dummy.climbStairs(45))
