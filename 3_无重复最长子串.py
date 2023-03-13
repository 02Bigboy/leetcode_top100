# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_d = {}
        i_start, max_num = 0, 0
        for i in range(len(s)):
            if s[i] in s_d:
                i_start = max(s_d[s[i]], i_start)    # 保存s[i]的字母已出现过的最新位置，即不重复的最新起始位置。
            max_num = max(max_num, i-i_start+1)      # 最长不含重复的，就是当前的位置，减去不重复的起始位置
            s_d[s[i]] = i+1                         # 更新字典
        return max_num


class Solution_:
    # 思想，保存每个字符出现的最新位置加一
    # 若前面已经出现过正在遍历的字符，则更新不重复的最新其实位置，就是上面保存的加一位置
    def sub_str(self, s):
        s_seen = {}
        no_repeat_start = 0
        max_len = 0
        for i in len(s):
            if s[i] in s_seen:
                no_repeat_start = max(s_seen[s[i]], no_repeat_start) # s[i] 已经出现过了，则更新不重复的最新起始位置。
            max_len = max(max_len, i - no_repeat_start + 1)
            s_seen[s[i]] = i + 1   # 因为出现过了，则应该往下面移一位
        return max_len
