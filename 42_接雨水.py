# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
class Solution:
    def trap(self, height: List[int]) -> int:
        # 思路：因此，对于每一根柱子，能接住雨水的量，就是左右两侧最高柱子的最小值与当前柱子的高度的差值，最后，将所有的柱子能接住的雨水量相加即可
        n = len(height)

        right = [0] * n
        right_max = 0
        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max

        left = [0] * n
        left_max = 0
        for i in range(n):
            left_max = max(left_max, height[i])
            left[i] = left_max
        
        total = 0
        for i in range(n):
            total += min(left[i], right[i]) - height[i]
        return total
    

class Solve:
    '''
    思路：每根柱子能接住的雨水，即是左右两侧最高柱子的的最小值，与当前柱子的差值
    然后把每根柱子的水量加起来就可以了
    '''
    def trap(height):
        n = len(height)
        right = [0]*n
        right_max = 0
        for i in range(n-1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max
        left = [0]*n
        left_max = 0
        for j in range(n):
            left_max = max(left_max, height[j])
            left[j] = left_max
        total = 0
        for i in range(n):
            total += min(right[i], left[i]) - height[i]
        return total 
