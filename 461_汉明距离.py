class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 转化成二进制，然后异或
        return bin(x^y).count("1")