# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划，s的前i位能否用dict表示
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
    

class Solve:
    '''
    思路：动态规划：s的前i位能否用dict表示，如果前i位能，则继续往后面找
    '''
    def wordbreak(s, worddict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in worddict):
                    dp[j] = True   # 我的理解是先找到s中左边的第一个单词（起点为0）在dict里，才继续找，继续找，起点就是第一个单词的终点+1
        return dp[-1]
