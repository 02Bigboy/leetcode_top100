# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 思想：每个值，与前面的所有值进行比较
        # 动态规划，dp[i]表示前i天的最大利润
        # 动态方程：dp[i] = max(dp[i-1], prince[i]-minprince)
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0] 

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]