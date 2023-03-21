# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 思路：将第n个也即最后一个括号，定位为最左端左括号组成的那一个括号
        # 则剩下的n-1个括号只能出现在第n个括号里，或者右侧
        # 所以p + q = n-1, 其中p表示出现在第n个括号里的括号，q表示出现在第n个括号右侧的括号
        # 所以遍历 p+q =n-1 就可以了
        if n == 0:
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []        
            for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]    # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:  
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]
    

class Solve:
    '''
    思路：把最后一个括号，定位成最左端左括号组成的括号
    则 剩下的n-1个括号要么在第n个括号里，要么在其右边
    所以遍历这两部分就可以了
    '''
    def kuohaos(n):
        if n == 0:
            return []
        total = []
        total.append([None])  # 0组括号时，记为None
        total.append(["()"])  # 一组括号只有一种情况
        for i in range(2, n+1):
            i_result = []
            for j in range(i):
                mid_list = total[j]
                right_list = total[i-1-j]
                for k1 in mid_list:
                    for k2 in right_list:
                        if k1 == None:
                            k1 = ''
                        if k2 = None:
                            k2 = ''
                        result = '(' + k1 + ')' + k2
                        i_result.append(result)
            total.append(i_result)
        return total[n]

# 本题还可以用回溯法：树的每个节点都可以取两个值，但是需要将一些结果去掉
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return []
                res = []

                def dfs(paths, left, right):
                    if left > n or right > left: return   # 右括号的数目不能大于左括号
                    if len(paths) == n * 2:  # 因为括号都是成对出现的
                        res.append(paths)
                        return

                    dfs(paths + '(', left + 1, right)  # 生成一个就加一个
                    dfs(paths + ')', left, right + 1)

                dfs('', 0, 0)
                return res