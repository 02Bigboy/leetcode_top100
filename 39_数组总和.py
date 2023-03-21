# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 思路：回溯法，生成一棵树，然后裁剪
        # y由于顺序任意，所以为了避免重复，则每一层对应位置不能再取左边已经取过的数，不然就会产生重复 如【2,2,3】【2,3,2】（当前数接左边的数，和左边的数接当前的数是一个效果）

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
    

class Solve:
    '''
    这个题一看就是回溯法，顺序任意，则要避免重复
    避免重复的办法：每一层对应位置当前数，不取左边的数去生成树
    '''
    def combinationSum(candidates, target):
        def find(candidates, left, right, path, out, target):
            if target < 0:
                return
            if target == 0:
                out.append(path)
                return
            for i in range(left, right):
                find(candidates, i, right, path + [candidates[i]], out, target - candidates[i])
        right = len(candidates)
        if right == 0:
            return []
        path = []
        out = []
        find(candidates, 0, right, path, out, target)
        return out
