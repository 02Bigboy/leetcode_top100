# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_num = len(nums1) + len(nums2)
        mid_num = all_num // 2   # 奇偶都要求这个值，求导第mid_num小值就可以了。
        serch_num = 0
        tem = 0 
        final = 0  # 记录上个略过的值
        i = 0
        j = 0
        while True:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    final = tem
                    tem = nums1[i]
                    
                    i += 1
                else:
                    final = tem
                    tem = nums2[j]
                    j += 1
            elif i < len(nums1):
                final = tem
                tem = nums1[i]
                i += 1
            else:
                final = tem
                tem = nums2[j]
                j += 1
            serch_num += 1
            if serch_num > mid_num:      # 就找到这里就可以了。
                break
        if all_num % 2 != 0:
            return tem
        else:
            return (tem + final) / 2
        
class Solve_:
    '''
    思路：求两个正序（从小到大）数列的中位数，等价于求到最小的中间那个数即可
    '''
    def midnum(self, nums1, nums2):
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        mid = (len_nums1 + len_nums2) // 2
        tem = final = 0
        i = j = 0   # 遍历nums1和nums2
        serch_count = 0
        while True:
            if i < len_nums1 and j < len_nums2:
                if nums1[i] < nums2[j]:
                    final = tem
                    tem = nums1[i]
                    i += 1
                else:
                    final = tem
                    tem = nums2[j]
                    j += 1
            elif i < len_nums1:
                final = tem
                tem = nums1[i]
                i += 1
            else:
                final = tem
                tem = nums2[j]
                j += 1
            
            serch_count += 1
            if serch_count > mid:
                break
        if (len_nums1 + len_nums2) % 2 != 0:  # 奇数
            return tem
        else:
            return (tem + final) / 2