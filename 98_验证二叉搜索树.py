# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 前序遍历--根节点大于左右两边
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
    
class Solve:
    def isvalid(self, root):
        def helper(node, left=float('-inf'), right=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= left or val >= right:
                return False
            
            if not helper(node.left, left, val):
                return False
            if not helper(node.right, val, right):
                return False
            return True
        return helper(root)