# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或：数组中的全部元素的异或运算结果即为数组中只出现一次的数字。
        # reduce函数先从列表（或序列）中取出2个元素执行指定函数，并将输出结果与第3个元素传入函数，输出结果再与第4个元素传入函数，…，以此类推，直到列表每个元素都取完。
        return reduce(lambda x, y: x ^ y, nums)
    
class Solve:
    '''
    思路：异或
    '''
    def singlenum(nums):
        return reduce(lambda x, y: x ^ y, nums)
