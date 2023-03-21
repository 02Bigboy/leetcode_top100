# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_n = {}
        num_len = len(nums)
        if num_len == 1:
            return nums[0]
        for i in range(num_len):
            if nums[i] not in dict_n:
                dict_n[nums[i]] = 1
            else:
                dict_n[nums[i]] += 1
                if dict_n[nums[i]] > num_len//2:
                    return nums[i]