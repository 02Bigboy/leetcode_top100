# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)    # 行数
        if m == 0:
            return False
        n = len(board[0]) # 列数
        mark = [[0 for _ in range(n)] for _ in range(m)]   # 标记是否使用过
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 找到单词的第一个元素
                    # 将该元素标记为已使用
                    mark[i][j] = 1   
                    if self.backtrack(i, j, mark, board, word[1:]) == True:   # 字符串或者list可以[n:],n可以大于len，返回的是空字符或list
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False
        
        
    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False



class Solve:
    '''
    思路：首先找到单词第一个字母在board中的位置，然后遍历四个方向，看看是否下一个字母能在资格方向找到，找到的话，继续深度
    '''
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def serchword(board, word):
        def dfs(i, j, used, board, word):
            if len(word) == 0:
                return True
            for dire in self.directs:
                cur_i = i + dire[0]
                cur_j = j + dire[1]
                if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                    if used[cur_i][cur_j] == 1:
                        continue
                    used[cur_i][cur_j] = 1
                    if dfs(cur_i, cur_j, used, board, word[1:]):
                        return True
                    else:
                        used[cur_i][cur_j] = 0
            return False
        row = len(board)
        if row == 0:
            return False
        lie = len(board[0])
        used = [[0]*lie for _ in range(row)]
        for i in range(row):
            for j in range(lie):
                if board[i][j] == word[0]:
                    if used[i][j] == 1:
                        continue
                    used[i][j] = 1
                    if dfs(i, j, used, board, word[1:]):
                        return True
                    else:
                        used[i][j] = 0
        return False

        

