# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 思路： 以i为结尾的前面和后面的乘积，的乘积
        dp_h = [1]*len(nums)
        dp_t = [1]*len(nums)
        for i in range(1,len(nums)):
            dp_h[i] = dp_h[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            dp_t[i] = dp_t[i+1] * nums[i+1]
        out = []
        for i in range(len(nums)):
            out.append(dp_h[i]*dp_t[i])
        return out
    

class Solve:
    def product(nums):
        len_nums = len(nums)
        res = []
        dp_h = [1] * len_nums
        dp_t = [1] * len_nums
        for i in range(1, len_nums):
            dp_h[i] = dp_h[i - 1] * nums[i-1]
        for j in range(len_nums-2, -1, -1):
            dp_t[i] = dp_t[i + 1] * nums[i+1]
        for i in range(len_nums):
            res.append(dp_h[i]*dp_t[i])
        return res
