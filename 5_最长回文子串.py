# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''思路：
                就按每个字符作为起始，寻找最大的字符串 与倒序相等
                temp 保存最大的字符串
                当寻找的字符串长度小于temp长度，就跳到下一个字符重新开始
        
        '''
        # verse_s = s[::-1]
        tem = s[0] # 存目前找的到最长的
        tem_num = 1
        for i in range(len(s)):
            j = len(s)                         # 从最长的字符串开始
            if len(s) - i <= tem_num:          # 字符串剩下的长度小于已找到的长度
                    break
            while j > i:
                if j - i <= tem_num:           # 以当前字符其实的长度小于已找到的长度
                    break
                if s[i:j] == s[i:j][::-1]:   # 与倒序相等
                    tem = s[i:j]
                    tem_num = len(tem)
                    break
                else:
                    j -= 1
        return tem
    

class Solve_:
    '''
    思路：以每个字符作为起始，寻找对应的最长子串
    找到了，则跳到下一个字符继续找
    '''
    def huiwen(s):
        tem = s[0]  # 保存最长子串
        len_tem = 1
        for i in range(len(s)):
            j = len(s)
            if len(s) - i <= len_tem:  # 如果剩下的字符串都没有已经找到的长了，就不需要找了
                break
            while j > i:              # 学到了用while替换for
                if j - i <= len_tem:  # 如果当前字符能查找的长度小于已经找到的最长的，就不需要找了
                    break
                if s[i:j] == s[i:j][::-1]:
                    tem = s[i:j]
                    len_tem = len(tem)
                    break
                else:
                    j -= 1
        return tem          
          