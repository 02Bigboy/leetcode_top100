# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 倒是可以两层循环遍历，但感觉会超时间限制
        ans = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            # 单调递减栈
            while stack and val > temperatures[stack[-1]]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        return ans