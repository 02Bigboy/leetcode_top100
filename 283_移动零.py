# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快排的思想：不等于0 的放左边，等于0 的放右边
        if not nums:
            return 0
		# 两个指针i和j
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1


class Solve:
    '''
    s思路：不等于0 的放左边
    '''
    def movezero(nums):
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
    