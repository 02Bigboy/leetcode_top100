# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 。
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 如果数组为空或 k = 0，直接返回空
        if not nums or not k:
            return []
        # 如果数组只有1个元素，直接返回该元素
        if len(nums) == 1:
            return [nums[0]]

        # 初始化队列和结果，队列存储数组的下标
        queue = []
        res = []

        for i in range(len(nums)):
            # 如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列
            if queue and queue[0] == i - k:
                queue.pop(0)

            # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()                              # 确保队列是个递减的
            # 新元素入队列
            queue.append(i)

            # 当前的大值加入到结果数组中
            if i >= k-1:
                res.append(nums[queue[0]])

        return res
    

class Solve:
    '''
    思路：保存一个队列，队列按照递减的顺序，新的数与队列比较，将小于新书的队列的数全都剔除，
    队列数间隔比k大时也要pop
    则当前窗的最大值：队列的第一个数
    '''
    def windowmax(nums, k):
        if not nums or not k:
            return []
        if len(nums) == 1:
            return nums
        
        queue = []
        res = []
        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res