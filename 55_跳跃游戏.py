# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置, 其实只用管能否到达最后一个位置即可
        return max_i>=i
    

class Solve:
    '''
    保存前面能跳到的最大位置，前面的最大位置至少要到达当前数，然后当前数能跳到的位置比最大值还大，就更新最大位置
    '''
    def canjump(nums):
        max_i = 0
        for i, jump in enumerate(nums):
            if max_i >=i and i+jump > max_i:
                max_i = i+jump
        return max_i >= i
