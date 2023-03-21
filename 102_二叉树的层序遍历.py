# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 思路：先将根节点放到队列中，然后不断遍历队列
        # 如果根节点的左右节点存在，又把它们放进队列里，先进先出，每层出根节点数
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            size = len(queue)
            tmp = []
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for _ in range(size):
                r = queue.pop(0)   # pop出第一个元素， 可以理解成先进先出
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            # 将临时list加入最终返回结果中
            res.append(tmp)
        return res
    

class Solve:
    def leveroder(root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            tem = []
            for i in range(size):
                val = queue.pop(0)    # 先进后出
                tem.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            res.append(tem)
        return res
