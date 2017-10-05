# -*- encoding: utf-8 -*-
# 给定 n 对括号，请写一个函数以将其生成新的括号组合，并返回所有组合结果。
# Example
# 给定 n = 3, 可生成的组合如下:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        str = ''
        left = 0
        right = 0
        maxi = n
        self.helper(array, str, left, right, maxi)
        return array

    def helper(self, array, str, left, right, maxi):  # 按一定规则往str里加左右括号，一旦长度为n*2了，就放array里
        if len(str) == maxi * 2:
            array.append(str)
            return
        if left < maxi:  # 如果left没都用了时，就加left
            self.helper(array, str + '(', left + 1, right, maxi)
        if right < left:  # 同时如果right比left少时，就加right
            self.helper(array, str + ')', left, right + 1, maxi)



class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        str = []
        left = 0
        right = 0
        maxi = n
        self.helper(array, str, left, right, maxi)
        return [''.join(ele) for ele in array]

    def helper(self, array, str, left, right, maxi):  # 按一定规则往str里加左右括号，一旦长度为n*2了，就放array里
        if len(str) == maxi * 2:
            array.append(str[:])
            return
        if left < maxi:  # 如果left没都用了时，就加left
            self.helper(array, str+['('], left + 1, right, maxi)
        if right < left:  # 同时如果right比left少时，就加right
            self.helper(array, str+[')'], left, right + 1, maxi)
        # 上面两部是基于原因input的，不是一个改完另一个接着改
if __name__ == "__main__":
    n = 3
    s = Solution1()

    print s.generateParenthesis(n)