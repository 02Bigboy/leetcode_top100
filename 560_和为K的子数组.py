# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和，包括加当前数
        # 要求的连续子数组
        count = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]
            
            # presum - (presun - k) = k, 所以有几个presum -k的值就加几个
            count += preSums[presum - k]   # 利用defaultdict的特性，当presum-k不存在时，返回的是0。这样避免了判断

            preSums[presum] += 1  # 给前缀和为presum的个数加1
            
        return count
    

class Solve:
    '''
    思路：前缀和
    两个前缀和之差等于k，这他们中间的连续数和就为K
    '''
    def subarry(nums, k):
        preSums = collections.defaultdict(int)   # 不存在时返回0
        preSums[0] = 1
        count = 0
        presum = 0
        for num in nums:
            presum += num
            count += preSums[presum - k]
            preSums[presum] += 1
        return count