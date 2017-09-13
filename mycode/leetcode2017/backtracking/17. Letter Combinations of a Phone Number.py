# -*- encoding: utf-8 -*-
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 例如
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# 给你一串按键，问能打出多少个组合，都是什么

# 方法1：backtracking法，从1开始，往里放2
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        tele = {
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        alfa = [] #把数字替换成对应字母串，存进这个array
        array = []
        for ele in digits:
            alfa.append(tele[ele])
        length = len(digits)
        # 变成了组合问题：从alfa里的每个字符串任取一个char组合成一个string，存res里，
        self.helper(alfa, res, array, length)
        return [''.join(ele) for ele in res]
    def helper(self, alfa, res, array, length):
        if len(array) == length: #如果array加到digits的长度了，就硬拷贝到res里
            res.append(array[:])
            return
        for i in range(len(alfa[0])):
            array.append(alfa[0][i])
            self.helper(alfa[1:], res, array, length)# 把其后面的那些组合了，alfa表现每次需要组合的
            array.pop()
# 方法2：比如是"12345"，就用1，2合并成新的1，然后跟345组合，再1，3合并成新1，跟4，5 组合，直到只剩1
class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        tele = {
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        alfa = [] #把数字替换成对应字母串，存进这个array
        for d in digits:
            alfa.append(list(tele[d]))
        alfa[0] = [list(ele) for ele in alfa[0]]
        for i in range(1,len(alfa)):
            alfa[0] = self.helper(alfa[0],alfa[i])  #把后面的ele往alfa的第一个ele里加
        return [ ''.join(ele) for ele in alfa[0]]

    def helper(self, a, b):
        res = []
        for ele_a in a:
            for ele_b in b:
                ele_a.append(ele_b)
                res.append(ele_a[:])
                ele_a.pop()

        return res
if __name__ == "__main__":
    d = '23'
    s = Solution1()
    print s.letterCombinations(d)