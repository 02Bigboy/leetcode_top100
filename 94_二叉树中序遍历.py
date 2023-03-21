# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# 递归遍历二叉树：
# 递归遍历太简单了

# 前序遍历：打印 - 左 - 右
# 中序遍历：左 - 打印 - 右
# 后序遍历：左 - 右 - 打印
# 终止条件 当前节点为空
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历	
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res
    

class Solve:
    def midoder(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res