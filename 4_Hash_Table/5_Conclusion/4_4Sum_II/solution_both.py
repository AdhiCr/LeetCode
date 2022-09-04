from typing import List
from collections import Counter, defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        count_nums3 = Counter(nums3)
        count_nums4 = Counter(nums4)

        nums1_nums2_sums = defaultdict(lambda: 0)
        nums3_nums4_sums = defaultdict(lambda: 0)

        for num1 in count_nums1:
            for num2 in count_nums2:
                nums1_nums2_sums[num1 + num2] += count_nums1[num1] * count_nums2[num2]

        for num3 in count_nums3:
            for num4 in count_nums4:
                nums3_nums4_sums[num3 + num4] += count_nums3[num3] * count_nums4[num4]

        counts = 0
        for val in nums1_nums2_sums:
            if -val in nums3_nums4_sums:
                counts += nums1_nums2_sums[val] * nums3_nums4_sums[-val]

        return counts


dummy = Solution()
print(dummy.fourSumCount(nums1=[1,2], nums2=[-2,-1], nums3=[-1,2], nums4=[0,2]))  # 2
print(dummy.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]))  # 1
print(dummy.fourSumCount([0,1,-1], [-1,1,0], [0,0,1], [-1,1,1]))  # 17