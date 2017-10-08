# -*- encoding: utf-8 -*-
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strs = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                res.append(strs[i])
        return ''.join(res)

if __name__ == "__main__":
    strs = 67
    s = Solution()
    print s.intToRoman(strs)