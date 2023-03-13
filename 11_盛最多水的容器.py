# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        思路3： 分别从两端开始取，哪端值小，就往中间走，直至两个端点重合，return面积最大即可。(宽度减小了，就看看高度有没有可能变大)
        '''
        max_s = 0
        h_left = 0
        h_right = len(height) - 1
        while h_left < h_right:
            s = (h_right - h_left) * min(height[h_left], height[h_right])
            if max_s < s:
                max_s = s
            if height[h_left] < height[h_right]:
                h_left += 1
            else:
                h_right -= 1
        return max_s


class Solve_:
    '''
    思路，分别从两端取值，哪端小，就往中间走，算每个面积，保留最大面积
    '''
    def max_val(height):
        max_s = 0
        left = 0
        right = len(height) - 1
        while left < right:
            s = (right - left) * min(height[left], height[right])
            if s > max_s:
                max_s = s
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_s
