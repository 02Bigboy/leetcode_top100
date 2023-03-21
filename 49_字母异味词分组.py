# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())
    

class Solve:
    '''
    思路就是用字典保存，每个字符串取了之后，先进行排序，则异味词排序后都是一样的，然后相应的字典加上这个字符串就好了
    '''
    def group(strs):
        mp = collections.defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())
