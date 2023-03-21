# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  
    
class Solve:
    '''
    思路：回溯法
    '''
    def subsets(nums):
        res = []
        n = len(nums)
        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res
