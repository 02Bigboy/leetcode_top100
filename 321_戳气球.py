# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

# 求所能获得硬币的最大数量。
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 动态规划：区间DP，开区间
        # 解析详见：https://leetcode.cn/problems/burst-balloons/solutions/2129246/312-chuo-qi-qiu-qu-jian-dp-javakotlinpyt-kq9c/
        # 定义f(i,j)为区间(i,j)所能取得的最大币值，那么显然f(0,n−1)是问题的解
        n = len(nums) + 2 # 两端是不爆破的
        self.coins = [1] * n
        for i in range(1, n - 1):
            self.coins[i] = nums[i - 1]
        self.mems = [[-1] * n for _ in range(n)] # 记忆，避免取不同最后一个爆破时，重复计算

        return self.collect_coins(0, n - 1)
    
    def collect_coins(self, left, right):
        if left >= right - 1:
            return 0
        if self.mems[left][right] != -1:
            return self.mems[left][right]
        best = 0
        tmp = self.coins[left] * self.coins[right]
        for k in range(left + 1, right):  # 遍历最后一个爆破的所有可能
            sk = self.coins[k] * tmp    # 把每个当成最后一个，所以需要乘两端
            sk += self.collect_coins(left, k) + self.collect_coins(k, right) # 还要加上两边区间的额
            best = max(best, sk)
        self.mems[left][right] = best
        return best
    

class Solve:
    '''
    思路，看成只剩下最后一个k气球了
    动态规划
    '''
    def maxcoins(nums):
        n = len(nums) + 2
        self.coins = [1] * n
        for i in range(1, n-2):
            self.coins[i] = nums[i-1]
        self.mem = [[-1] * n for _ in range(n)]  # 避免重复计算
        return self.collect_coins(0, n-1)
    def collect_coins(left, right):
        if left >= right:
            return 0
        if self.mem[left][right] != -1:
            return self.mem[left][right]
        best = 0
        tem = self.coins[left] * self.coins[right]
        for k in range(left+1, right):
            sk = self.coins[s] * tem
            sk = sk + self.collect_coins(left, k) + self.collect_coins(k, right) 
            best = max(sk, best)
        self.mem[left][right] = best
        return best