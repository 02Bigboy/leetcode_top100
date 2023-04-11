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