# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 思路：时间复杂度为log n 应该想到二分法查找
        # 本来是有序数列，旋转了一下，分一半，其中有一半必然为有序的，对于有序的那一半只需要比较端点就行了
        if not nums:
            return -1
        l, r = 0, len(nums) - 1  # 初始化左右端点
        while l <= r:
            mid = (l + r) // 2   # 二分
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:    # 左一半是有序的话
                if nums[0] <= target < nums[mid]:
                    r = mid - 1         # 在左半边里
                else:
                    l = mid + 1         # 在右半边里
            else:                       # 右一半是有序的话
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    

class Solution:
    '''
    题目说道时间复杂度logn，所以要想到用二分法
    思路：旋转的数列，有一半是有序的，有序的只用比较端点就行了
    用二分法查找
    '''
    def serch(nums, target):
        if not nums:
            return -1
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 左端点有序
                if nums[0] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1
        

