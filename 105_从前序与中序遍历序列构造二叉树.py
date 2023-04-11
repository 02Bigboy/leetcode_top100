# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， 
# inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 思路：preorder第一个元素为root，在inorder里面找到root，在它之前的为左子树（长l1），
        # 之后为右子树（长l2）。preorder[1]到preorder[l1]为左子树,之后为右子树，分别递归。
        if not (preorder and inorder):
			return None
		# 根据前序数组的第一个元素，就可以确定根节点	
		root = TreeNode(preorder[0])
		# 用preorder[0]去中序数组中查找对应的元素
		mid_idx = inorder.index(preorder[0])
		# 递归的处理前序数组的左边部分和中序数组的左边部分
		# 递归处理前序数组右边部分和中序数组右边部分
		root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])       # 什么时候要用self?
		root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
		return root
