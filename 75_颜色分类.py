# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 冒泡?
        from typing import List

        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return nums

        zero = 0
        two = size

        i = 0

        while i < two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(nums, i, two)
        return nums


class Solve:
    '''
    思路：依次遍历，0就放到左边去，2就右边，1就不变
    '''
    def sortcolor(self, nums):
        def swap(nums, index1, index2):
            # 交换
            nums[index1], nums[index2] = nums[index2], nums[index1]

        zero = 0
        second = len(nums) - 1
        i = 0
        while i <= second:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, second)
                second -= 1
        return nums
