from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(array, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and array[i] < array[l]:
                largest = l
            if r < n and array[largest] < array[r]:
                largest = r

            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                heapify(array, n, largest)

        n = len(nums)
        for i in range(n // 2, -1, -1):
            heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
        return nums