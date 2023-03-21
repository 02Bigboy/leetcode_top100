; 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

; 路径和 是路径中各节点值的总和。

; 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 思路：计算二叉树中的一个节点的最大贡献值，具体而言，就是在以该节点为根节点的子树中寻找以该节点为起点的一条路径，使得该路径上的节点值之和最大
def maxGain(node):
    if not node:
        return 0

    # 递归计算左右子节点的最大贡献值
    # 只有在最大贡献值大于 0 时，才会选取对应子节点
    leftGain = max(maxGain(node.left), 0)
    rightGain = max(maxGain(node.right), 0)
    
    # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
    priceNewpath = node.val + leftGain + rightGain
    
    # 更新答案
    self.maxSum = max(self.maxSum, priceNewpath)

    # 返回节点的最大贡献值
    return node.val + max(leftGain, rightGain)

self.maxSum = root.val
maxGain(root)
return self.maxSum