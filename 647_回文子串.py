# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

# 回文字符串 是正着读和倒过来读一样的字符串。

# 子字符串 是字符串中的由连续字符组成的一个序列。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 区间i-j是不是回文
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result