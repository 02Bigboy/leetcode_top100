; 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

; 测试用例的答案是一个 32-位 整数。

; 子数组 是数组的连续子序列。
# 乘积就与和不一样，因为负的后面再遇到负的就成了正的了
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 思路：求出以每个数为结尾的最大和最小值
        if not nums: return 
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

class Solve:
    def maxpoint(nums):
        if not nums:
            return
        res = num[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max*num, pre_min*num, num)
            cur_min = min(pre_max*num, pre_min*num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

