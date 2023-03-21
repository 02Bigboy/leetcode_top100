# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 思路
        # lower_bound 返回最小的满足 nums[i] >= target 的 i
        # 如果数组为空，或者所有数都 < target，则返回 len(nums)
        # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

        # 闭区间写法
        def lower_bound(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1  # 闭区间 [left, right]
            while left <= right:  # 区间不为空
                # 循环不变量：
                # nums[left-1] < target
                # nums[right+1] >= target
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1  # 范围缩小到 [mid+1, right]
                else:
                    right = mid - 1  # 范围缩小到 [left, mid-1]
            return left  # 或者 right+1

        start = lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 如果 start 存在，那么 end 必定存在
        end = lower_bound(nums, target + 1) - 1
        return [start, end]


class Solve:
    '''
    思路：编写一个函数，返回num[i] >= target的最小的i
    一看题目：log(n)又是二分法
    '''
    def searchange(nums, target):
        def findi(nums, target):
            left, right = 0, len(nums) - 1   #得到的是一个>=target的闭区间
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return left    # 都大于target则，返回0，都小于则返回len(nums),有num[i] >=target,则返回最小的i
        start = findi(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        else:
            end = findi(nums, target + 1) - 1
            return [start, end] 