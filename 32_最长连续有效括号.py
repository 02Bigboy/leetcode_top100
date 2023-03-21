# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 思路：先找到所有匹配项的位置，然后对位置进行排序，找出最长的连续数列的长度就行了
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort()
        #print(res)
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:      # 寻找连续的最长数列
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans
    

class Solve:
    '''
    思路：先找到正确的括号，然后再对找到的括号位置进行排序，然后找到最长的连续数列就可以了
    '''
    def validright(s):
        if not s:
            return 0
        stack = []
        res = []
        for i in range(len(s)):
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
            if s[i] == '(':
                stack.append(i)
        res.sort()
        # 找出最长的连续数列：以i为左端点的最长数列
        i = 0
        max_out = 0
        while i < len(res):
            j = i
            while j < len(res) - 1 and res[j + 1] == res[j] + 1:
                j += 1
            max_out = max(max_out, j - i + 1)
            i = j + 1
        return max_out
        
