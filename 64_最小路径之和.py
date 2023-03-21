# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 思路：动态规划：
        # dp[i][j]表示到达[i][j]位置的总和最小值
        # 动态方程：dp[i][i] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # 第一行和第一列都是前面的累加
        row_= len(grid)
        list_ = len(grid[0])
        dp = grid
        dp[0][0] = grid[0][0]
        for i in range(1, row_):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, list_):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, row_):
            for j in range(1, list_):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
    

class Solve:
    '''
    思路：动态规划
    dp[i][j]：表示走到ij位置的最小总和
    动态方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    初始化：第一行和第一列都是前面的累加和
    '''
    def minpathsum(grid):
        row = len(grid)
        lie = len(grid[0])
        dp = grid
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, lie):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, row):
            for j in range(1, lie):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

