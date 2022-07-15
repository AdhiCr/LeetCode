from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            # if nums1 is empty, assign nums2 to nums 1
            for idx, val in enumerate(nums2):
                nums1[idx] = val
        elif n == 0:
            # if nums2 is empty, nothing has to be done
            pass
        else:
            order_dict = {}
            order_dict_idx = len(nums1) - 1
            num_1_idx, num_2_idx = 0, 0
            while (num_1_idx + num_2_idx) < (m + n):
                if num_1_idx == m:
                    order_dict[order_dict_idx] = nums2[n - num_2_idx - 1]
                    num_2_idx += 1
                elif num_2_idx == n:
                    order_dict[order_dict_idx] = nums1[m - num_1_idx - 1]
                    num_1_idx += 1
                elif nums1[m - num_1_idx - 1] > nums2[n - num_2_idx - 1]:
                    order_dict[order_dict_idx] = nums1[m - num_1_idx - 1]
                    num_1_idx += 1
                else:
                    order_dict[order_dict_idx] = nums2[n - num_2_idx - 1]
                    num_2_idx += 1

                order_dict_idx -= 1

            for i in range(len(nums1)):
                nums1[i] = order_dict[i]


dummy = Solution()
dummy.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)


"""
[1,2,3,0,0,0]
3
[2,5,6]
3
Output:
[2,5,6,2,5,6]
Expected:
[1,2,2,3,5,6]
"""