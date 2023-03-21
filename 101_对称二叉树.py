# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(left, right):
            # 递归的终止条件是两个节点都为空
            # 或者两个节点中有一个为空
            # 或者两个节点的值不相等
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
		# 用递归函数，比较左节点，右节点
        return dfs(root.left,root.right)
    

class Solve:
    def isSymmetric(self, root):
        if not root:
            return True
        def dfs(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)