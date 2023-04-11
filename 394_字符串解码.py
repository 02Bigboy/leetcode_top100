# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入
class Solution:
    def decodeString(self, s: str) -> str:
        # 思路：构建辅助栈，进栈出栈
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':   # 有些数字不止0-9
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res
    

class Solution:
    '''
    构建辅助栈，进栈出栈
    '''
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                multi = 0
                res = ""
            elif c == ']':
                cur_multi, cur_res = stack.pop()
                res = cur_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi*10 + c
            else:
                res += c
        return res