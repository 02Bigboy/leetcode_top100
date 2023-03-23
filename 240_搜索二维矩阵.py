# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1

        while 0<=i<m and 0<=j<n and matrix[i][j] != target:
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                
        return 0<=i<m and 0<=j<n and matrix[i][j] == target