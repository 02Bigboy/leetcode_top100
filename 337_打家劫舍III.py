# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 由下至上
        # 偷当前节点：则收益为：偷当前节点+不偷左右子树
        # 不偷当前节点：则收益为：左右子树各自最大值之和
        def DFS(root):
            if not root:
                return 0, 0
            # 后序遍历
            leftchild_steal, leftchild_nosteal = DFS(root.left)
            rightchild_steal, rightchild_nosteal = DFS(root.right)

            # 偷当前node，则最大收益为【投当前节点+不偷左右子树】
            steal = root.val + leftchild_nosteal + rightchild_nosteal
            # 不偷当前node，则可以偷左右子树
            nosteal = max(leftchild_steal, leftchild_nosteal) + max(rightchild_steal, rightchild_nosteal)
            return steal, nosteal
            
        return max(DFS(root))
    

class Solve:
    def rob(root):
        def DFS(root):
            if not root:
                return 0, 0
            left_steal, left_nots = DFS(root.left)
            right_steal, right_nots = DFS(root.right)
            steal = root.val + left_nots + right_nots
            nosteal = max(left_steal, left_nots) + max(right_steal, right_nots)
            return steal, nosteal
        return max(DFS(root))
        