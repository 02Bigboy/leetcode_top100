# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
class Solution:
    # 每行当成二进制数，然后相与，与的行数就是高，与的连续1的个数就是宽
    def getWidth(self,num):  #步骤3：求一个数中连续最多的1
        w=0
        while num>0:
            num&=num<<1
            w+=1
        return w
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums=[int(''.join(n),base=2) for n in matrix]  #步骤1：**每一行当作二进制数**
        res,n=0,len(nums)
        for i in range(n):   #步骤2：枚举所有的组合，temp存储相与的结果
            temp=nums[i]
            for j in range(i,n):
                temp&=nums[j]
                w=self.getWidth(temp)
                h=j-i+1
                res=max(res,min(w,h))
        return res*res
    

class Solve:
    '''
    思路：将每一行看成一个二进制数，然后相与
    相与结果的连续1的个数就是长，相与的行数就是高
    '''
    def maxs(matrix):
        def gitwidth(nums):
            # 返回二进制数连续1的个数
            w = 0
            while nums:
                nums &=nums << 1
                w += 1
            return w
        
        nums = [int(''join(n), base=2) for n in matrix]
        max_s, n = 0, len(nums)
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp &= nums[j]
                w = gitwidth(temp)
                h = j - i + 1
                max_s = max(max_s, min(w, h))
        return max_s*max_s