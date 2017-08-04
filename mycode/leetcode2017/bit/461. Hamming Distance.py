# -*- encoding: utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        bit_x = self.trans(x)
        bit_y = self.trans(y)
        if len(bit_x) < len(bit_y):
            bit_x = [0] * (len(bit_y) - len(bit_x)) + bit_x
        if len(bit_x) > len(bit_y):
            bit_y = [0] * (len(bit_x) - len(bit_y)) + bit_y
        i = 0
        while i < len(bit_x):
            if bit_x[i] != bit_y[i]:
                ans += 1
            i +=1
        return ans

    def trans(self, x):
        array = []
        while x / 2 != 0:
            array.insert(0, x % 2)
            x = x/2
        array.insert(0, x % 2)
        return array

class Solution_leet(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x^y
        ans = bin(int(str(a),10))
        # bin(int('4', 10)) = 0b100 注意：这里的0b100，其实就是100，0b的b是binary的意思
        return ans.count('1')
if __name__ == "__main__":
    a = 1
    b = 4
    x = Solution_leet()
    print x.hammingDistance(a,b)
