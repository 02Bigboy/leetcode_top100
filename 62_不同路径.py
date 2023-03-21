# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 思路：动态规划
        # dp[i][j]表示到达[i][j]位置的最多路径
        # 动态方程：dp[i]][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]   # 第一行和第一列都只有一条路径
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    

class Solve:
    '''
    思路：动态规划：
    dp[i][j]:到达位置ij的最多路径
    动态方程：dp[i]][j] = dp[i-1][j] + dp[i][j-1]
    初始化：第一行和第一列都是1
    '''
    def uniquepaths(m, n):
        dp = [[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
