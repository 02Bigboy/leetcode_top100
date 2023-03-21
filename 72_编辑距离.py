# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 动态规划：
        # dp[i][j] 表示代表 word1 **到** i 位置转换成 word2 到 j 位置需要最少步数
        # 向下表示删除
        # 向右表示插入
        # 向右下表示替换
        # 动态方程： dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # 第一行（word1为空）都是插入操作，第一列（word2为空）都是删除操作
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
    

class Solve:
    '''
    向右表示插入
    向下表示删除
    向右下表示替换
    思路：动态规划
    dp[i][j]表示：word1 到i能到word2 到j 的最小操作数
    动态方程：
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1]dp[j-1]) + 1
    初始化：第一行全是插入，第一列全是删除
    初始化加一个空字符
    '''
    def transfer(word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]