# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

# 返回所有可能的结果。答案可以按 任意顺序 返回
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = []

        @lru_cache(None)
        def dfs(idx, cl, cr, dl, dr, path):
            if idx == len(s):
                if not dl and not dr:
                    ans.append(path)
                return
            if cr > cl or dl < 0 or dr < 0:
                return
            c = s[idx]
            if c == '(':
                dfs(idx+1,cl,cr,dl-1,dr, path)
            elif c == ')':
                dfs(idx+1,cl,cr,dl,dr-1, path)
            dfs(idx+1,cl+(c=='('),cr+(c==')'),dl,dr, path+c)
        
        dfs(0, 0, 0, l, r, "")
        return ans
