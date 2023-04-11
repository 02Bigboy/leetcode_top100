# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

# 你可以认为每种硬币的数量是无限的。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 动态规划：
        # dp[n] = dp[n-coin] + 1, coin in coins
        # 备忘录
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            
            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        
        return dp(amount)
    

class Solve:
    '''
    动态规划：dp[n] = dp[n - coin] + 1
    '''
    def coincount(coins, amount):
        memo = dict{}    # 避免重复计算
        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1: continue
                res = min(res, subproblem + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        return dp[amount]
