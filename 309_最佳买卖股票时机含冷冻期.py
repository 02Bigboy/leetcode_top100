# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划：思路：每次有两个选择（）
        # 定义 dp[i][j] 为第 i+1 天所能获得的最大收益，其中 0≤j≤1，j=0表示第 i+1 天不持股，j=1 表示第 i+1 天持股。
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], (0 if i - 2 < 0 else dp[i - 2][0]) - prices[i])
        return dp[n - 1][0]
    

class Solve:
    '''
    思路，动态规划
    每个节点有两种状态，持有股票或者不持有
    dp[i][j], j=0表示第i+1天不持有股票，j=1表示持有股票
    '''
    def maxgup(prices):
        # 初始化：
        dp = [[0]*2 for _ in prices]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # i + 1天不持有股票 = i天不持有股票，i天持有股票，然后i+1天卖掉了
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # i+1天持有股票 = i天持有股票， i天不持有股票（i天原始就没有，**NOTE 而不是卖掉了**，因为卖掉了有冷冻期i+1天就不能买了）+ 买i+1天股票
            dp[i][1] = max(dp[i-1][1], (0 if i-2 < 0 else dp[i-2][0] - prices[i]))
        return dp[-1][0]
