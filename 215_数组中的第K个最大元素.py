# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution:
    '''
    思路：找第K个最大元素即找最小的n-k+1元素
    按某个数进行分：小于他的放到左边，大于他的放到右边
    那个数的位置与n-k+1比较，大于则在左边继续找，小于则在右边继续找
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr: List[int], low: int, high: int) -> int:
            pivot = arr[low]                                        # 选取最左边为pivot

            left, right = low, high     # 双指针
            while left < right:
                
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处
                
                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处
            
            arr[left] = pivot           # pivot放置到中间left=right处
            return left
        
        def randomPartition(arr: List[int], low: int, high: int) -> int:
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            return partition(arr, low, high)                        # 调用partition函数

        def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
            # mid = partition(arr, low, high)                   # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)               # 以mid为分割点【随机选择pivot】
            if mid == k-1:                                      # 第k小元素的下标为k-1
                return arr[mid]                                 #【找到即返回】
            elif mid < k-1:
                return topKSplit(arr, mid+1, high, k)           # 递归对mid右侧元素进行排序
            else:
                return topKSplit(arr, low, mid-1, k)            # 递归对mid左侧元素进行排序
        
        n = len(nums)
        return topKSplit(nums, 0, n-1, n-k+1)                   # 第k大元素即为第n-k+1小元素
    

class Solution:
    '''
    思路：找第K个最大元素即找最小的n-k+1元素
    按某个数进行分：小于他的放到左边，大于他的放到右边
    那个数的位置与n-k+1比较，大于则在左边继续找，小于则在右边继续找
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def split(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left<right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left<right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        def randsplit(nums, low, hight):
            pivot_id = random.randint(low, high)
            nums[low], nums[pivot_id] = nums[pivot_id], nums[low]
            return split(nums, low, hight)
        def topkSplit(nums, low, high, k):
            mid = randsplit(nums, low, high)
            if mid == k-1:
                return nums[mid]
            elif mid < k -1:
                return topkSplit(nums, mid+1, high, k)
            else:
                return topkSplit(nums, low, mid - 1, k)
        return topkSplit(nums, 0, len(nums) - 1, n-k+1)
            
