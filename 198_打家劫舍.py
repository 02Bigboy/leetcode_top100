# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划
        # dp[n+1]=max(dp[n],dp[n−1]+num)
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
    

class Solve:
    '''
    思路：动态规划
    dp[n+1] = max(dp[n], dp[n-1]+num)
    '''
    def rob(nums):
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(cur, pre+num), cur
        return cur
