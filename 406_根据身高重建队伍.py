# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。

# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 思路：先进行升高的降序排列是关键，才会让题变简单
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))  # 按升高降序排列
        for p in people:
            if len(res) <= p[1]:     # 前面的长度下雨等于需要的人数
                res.append(p)
            elif len(res) > p[1]:    # 超过了，则需要插到前面去
                res.insert(p[1], p)
        return res