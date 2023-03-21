# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组 是数组中的一个连续部分。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 以每个数结尾的连续子数组最大和：
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
    

class Solve:
    '''
    思路：以每个数作为结束值的最大子数组和
    '''
    def maxsplitarrary(nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        dp = [0] * len_nums
        dp[0] = nums[0]
        for i in range(1, len_nums):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
