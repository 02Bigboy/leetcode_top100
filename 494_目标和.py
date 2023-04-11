# 给你一个整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #  符号为正的元素和计为x，符号为负的元素和计为y
        #这个题转化为x=(s+target)/2, 所有该问题等价于从数组里选出一部分元素使其和为x
        # 动态规划
        # 这道题和416. 分割等和子集好像，转化为背包问题
        s = sum(nums)
        # 去除x不是整数和target绝对值超过s的情况
        if (s+target)%2 or abs(target) > s: return 0
        cap = (s+target)//2
        dp = [0]*(cap+1)
        dp[0] = 1 #不选任何元素时和为0，所以有1种情况
        for n in nums:
            # 倒序更新
            for i in range(cap,n-1,-1):
                dp[i] += dp[i-n]
        return dp[cap]