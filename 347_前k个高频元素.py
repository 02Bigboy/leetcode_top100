# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        out = []
        for i in range(k):
            out.append(dic[i][0])
        return out
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list = {}
        for num in nums:
            if num in dict_list:
                dict_list[num] += 1
            else:
                dict_list[num] = 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        out = []
        for i in range(k):
            out.append(dic[i][0])
        return out