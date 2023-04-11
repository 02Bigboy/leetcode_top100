# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 请你找出符合题意的 最短 子数组，并输出它的长度。
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy_nums = nums.copy()
        copy_nums.sort()#浅复制并排序
        answer = 0
        long_nums = len(nums)
        c = []
        for i in range(long_nums):#对比排序前后数组产生变化了的下标
            if copy_nums[i] != nums[i]:
                c.append(i)
        if len(c) == 0:
            return answer #如果无变化直接返回零
        else:
            answer = c[-1] - c[0] + 1 #max(c) - min(c) + 1 #有变化则最短无序数组为下标最小处到下标最大处。
        return answer


class Solve:
    '''
    思路：复制一份，对复制的进行排序，然后比较，保留不同的位置序号，最大的-最小的序号+1
    '''
    def paixu(nums):
        cop = nums.copy()
        cop.sort()
        out = 0
        c = []
        for i in range(len(nums)):
            if nums[i] != cop[i]:
                c.append(i)
        if len(c) == 0:
            return out
        return c[-1] - c[0] + 1