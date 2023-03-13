# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
class Solution(object):
    def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            cach = {}
            for index, i in enumerate(nums):
                if target - i in cach:
                    return [cach[target - i], index]  # 查找keys()的时间会很长。 不用keys也可以找。
                else:
                    cach[i] = index

def twosum(nums, target):
    cach = {}
    for index, num in enumerate(nums):
        if target - num in cach:
            return [cach[target - num], index]
        else:
            cach[num] = index

# 次此代码学到的就是用enumerate遍历数组，返回的是index，value的格式