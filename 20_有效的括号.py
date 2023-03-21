# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
class Solution:
    def isValid(self, s: str) -> bool:
        # 思路：首先字符串长度要是双数，然后从左到右比较下一个是否相同，相同则跳俩
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
    

class Solve:
    def isgood(s):
        if '()' in s or '[]' in s or '{}' in s:
            s.replace('()', '')
            s.replace('[]', '')
            s.replace('{}', '')
        return s == ''