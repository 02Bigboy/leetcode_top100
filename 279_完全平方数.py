# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
# 例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i]的值为和为 i 的完全平方数的最少数量，我们从1开始一直算到n，每次dp[i]等于所有能再加一个完全平方数等于i的值中的最小值，dp中最后一个元素就是我们要寻找的和为 n 的完全平方数的最少数量。
        #dp[i]的值为和为 i 的完全平方数的最少数量
        dp=[n]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            #m为最大的整数使得其平方小于等于i
            m=int(pow(i,0.5))
            #遍历所有能一步到达i的值中的最小值
            for j in range(1,m+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]
    

class Solve:
    '''
    思路：动态规划
    dp[i] 表示和为i的完全平方数的最少数量
    dp[i] 再加一个完全平方数等于i 的dp +1
    '''
    def numsqure(self, n):
        dp = [n] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            sq = int(pow(i, 0.5))
            for j in range(1, sq+1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]
