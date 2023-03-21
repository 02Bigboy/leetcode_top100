# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums) # 哈希表存储数组中的数，这样查看一个数是否存在即能优化至 O(1)O(1)O(1) 的时间复杂度

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    

class Solve:
    '''
    思路：找出以每个点为起点的最长序列，取里面的最长
    '''
    def longcons(nums):
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len

