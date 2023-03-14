# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 思路2：回溯法，一棵树，取到最下面
        # 首先定义字典
        dict_num = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        out = []
        digits_lens = len(digits)
        if digits_lens == 0 or digits_lens > 4:
            return out
        
        def back(out, index, temp):
            if index == digits_lens:
                out.append(temp)
                # temp = ""
                return   # return 就是回溯法，每条路的终止寻找处
            for i in dict_num[digits[index]]:
                a = temp + i
                back(out, index + 1, a)
        back(out, 0, "")
        return out
    
class Solve:
    '''
    思想：回溯法，深度优先，
    回溯法可以看成生成了一棵树
    每一层就相当于每个电话号码数字能代表的字母
    '''
    def phonenums(digits):
        # 字典
        dict_num = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        out = []
        len_nums = len(digits)
        if len_nums == 0 or len_nums > 4:
            return out
        def tree(out, index, tem):
            # 输入：输出结果，层数，以及保存的中间结果
            if index == len_nums:
                out.append(tem)
                return
            for i in dict_num[digits[index]]:
                a = tem + i
                tree(out, index + 1, a)
        
        tree(out, 0, '')
        return out

