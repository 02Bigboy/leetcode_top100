# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[n] = dp[n-1] + dp[n-2]
        if n < 3:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    

class Solve:
    '''
    思路动态规划
    dp[n] = dp[n-1] + dp[n-1]
    dp[0] = 1
    dp[1] = 2
    '''
    def climbstairs(n):
        if n < 3:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
