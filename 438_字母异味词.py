# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        n, m = len(s), len(p)
        if m > n:
            return []
        
        cnt = collections.Counter(p)    # 哈希表：记录需要匹配到的各个字符的数目
        need = m                        # 记录需要匹配到的字符总数【need=0表示匹配到了】
        res = []

        for right in range(n):
            
            # 窗口右边界
            ch = s[right]               # 窗口中新加入的字符
            if ch in cnt:               # 新加入的字符位于p中
                if cnt[ch] > 0:         # 此时新加入窗口中的字符对need有影响
                    need -= 1
                cnt[ch] -= 1
            
            # 窗口左边界
            left = right - m
            if left >= 0:
                ch = s[left]
                if ch in cnt:           # 刚滑出的字符位于p中
                    if cnt[ch] >= 0:    # 此时滑出窗口的字符对need有影响
                        need += 1
                    cnt[ch] += 1

            if need == 0:           # 找到了一个满足题意的窗口，其左端点为right-m+1
                res.append(right - m +1)
        
        return res