# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 用sumlist记录了从当前节点往回走的各个长度的路径的和
        def dfs(root, sumlist):
            if root is None: return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(targetSum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])