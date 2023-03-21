# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        mxarea = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                mid = stack.pop()
                area = heights[mid] * (i - 1 - stack[-1])
                if area > mxarea: mxarea = area
            stack.append(i)
        return mxarea