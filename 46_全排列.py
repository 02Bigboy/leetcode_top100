# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        path = []
        dfs(nums, size, 0, path, used, res)
        return res
    

class Solve:
    '''
    思路：就是回溯法，但是需要减枝，就是每条路而言，前面已经用过的数就不能再用了
    '''
    def permute(nums):
        def dfs(nums, size, depth, used, path, out):
            if depth == size:
                out.append(path)
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    dfs(nums, size, depth+1, used, path + [nums[i]], out)
                    used[i] = False

        size = len(nums)
        used = [False for _ in range(size)]
        path = []
        out = []
        dfs(nums, size, 0, used, path, out) 
        return out           
