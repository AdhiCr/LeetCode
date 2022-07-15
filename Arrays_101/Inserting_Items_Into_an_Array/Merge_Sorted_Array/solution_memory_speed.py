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
            edit_idx = -1
            num_1_idx, num_2_idx = m, n
            while (num_1_idx + num_2_idx) > 0:
                if num_1_idx == 0:
                    nums1[edit_idx] = nums2[num_2_idx - 1]
                    num_2_idx -= 1
                elif num_2_idx == 0:
                    nums1[edit_idx] = nums1[num_1_idx - 1]
                    num_1_idx -= 1
                elif nums1[num_1_idx - 1] > nums2[num_2_idx - 1]:
                    nums1[edit_idx] = nums1[num_1_idx - 1]
                    num_1_idx -= 1
                else:
                    nums1[edit_idx] = nums2[num_2_idx - 1]
                    num_2_idx -= 1

                edit_idx -= 1


dummy = Solution()
dummy.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)