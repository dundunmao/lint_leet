# -*- encoding: utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        #把10进制转成2进制，这里是array
        bit_x = self.trans(x)
        bit_y = self.trans(y)
        # 补位，让两个数的位数相同，少位数的前面加0
        if len(bit_x) < len(bit_y):
            bit_x = [0] * (len(bit_y) - len(bit_x)) + bit_x
        if len(bit_x) > len(bit_y):
            bit_y = [0] * (len(bit_x) - len(bit_y)) + bit_y
        i = 0
        # 同步遍历找不同
        while i < len(bit_x):
            if bit_x[i] != bit_y[i]:
                ans += 1
            i +=1
        return ans

    def trans(self, x): #把10进制转成2进制
        array = []
        while x / 2 != 0:
            array.insert(0, x % 2)
            x = x/2
        array.insert(0, x % 2)
        return array

class Solution_leet(object):
    def hammingDistance(self, x, y):
        return  bin(x^y).count('1') #x^y取二进制的交集并转成十进制。所以bin(x^y)是交集的二进制结果
if __name__ == "__main__":
    a = 1
    b = 4
    x = Solution_leet()
    print x.hammingDistance(a,b)
