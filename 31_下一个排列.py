# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。

# 必须 原地 修改，只允许使用额外常数空间。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 这个题的意思就是找到所有排列比目前排列组成的数大一点的下一个数的排列
        # 思路：从后往前查找（从低位变换，增的值最小），当a[i]<a[i+1]就找到i了，这个i就是要变的位置，
        # 然后还是从后往前查找（从小的开始找，因为上面那种查找方式得到的右边区间肯定是降序）（i+1,n）找到第一个数使得
        #a[i]<a[j],然后交换a[i],a[j]的位置就好了。最后再对a[i]后面的数升序排列就好了。
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:      # 找i
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:      # 找j
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]       # 交换
        
        left, right = i + 1, len(nums) - 1
        while left < right:           # 倒序
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class Solve:
    '''
    思路：题的意思就是找到比目前排列大一点点的排列
    做法：从后往前查找，当nums[i] < nums[j]的时候就找到了如何只变大一点点的位置
    然后，还是从后往前找，找到第一个比nums[i]大的位置j，   (说明：i+1, 到末尾是个降序排列)
    交换nums[i], nums[j]
    然后再把位置i后的数倒序一下就行了  因为交换ij后，i后的数还是倒序
    '''

    def next_list(nums):
        i = len(nums) - 2
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >=0:
            j = len(nums) - 1
            while j >=0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 对i后面的数倒序
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
