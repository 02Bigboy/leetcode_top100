# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

# 你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        思路2：可以先进行排序,然后遍历每个数，看看后边有没有两个数之和，等于当前数的负数
        '''
        nums.sort()
        len_nums = len(nums)
        out = []
        for first in range(len_nums):
            # if nums[first] > 0:
            #     break
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = len_nums - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, len_nums):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:   # 这一步比较有意思
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    out.append([nums[first], nums[second], nums[third]])
        return out
    

class Solve:
    '''
    思路：先排序，在从左到右遍历，看看每个数右边有没有两个数之和等于当前数的负数
    '''

    def sumthreenums(nums):
        nums.sort()
        len_nums = len(nums)
        out = []
        for first in range(len_nums):
            # 需要和上一次枚举数不同，相同则结果会有重复
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] > 0:
                break   # 排序了的，所以都大于0了，就没有满足条件的了
            target = -nums[first]
            third = len_nums - 1   # 第三个数从最右边往左
            for second in range(first+1, len_nums):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break  # 当前的second 域third的和都一直大于target，后面的只会更大
                if nums[second] + nums[third] == target:
                    out.append([nums[first], nums[second], nums[third]])
        return out
