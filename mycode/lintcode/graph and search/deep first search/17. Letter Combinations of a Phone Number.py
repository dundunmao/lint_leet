class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        h = {
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
        m = []
        array = []
        for ele in digits:
            m.append(h[ele])
        length = len(digits)
        row = 0
        self.helper(m, res, array, length, row)
        return [''.join(ele) for ele in res]

    def helper(self, m, res, array, length, row):
        if len(array) == length:
            res.append(array[:])
            return
        for i in range(len(m[row])):
            array.append(m[row][i])

            self.helper(m[row+1:], res, array, length, row)
            array.pop()


class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        h = {
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

        new = list(digits[0])
        for i in range(1,len(digits)):
            new = self.combination(new,digits[i])
        return new
    def combination(self, s1, s2):
        res = []
        for ele in s1:
            for e in s2:
                res.append([ele,e])
        return res

if __name__ == '__main__':
    s = Solution()
    x = '12'
    print s.letterCombinations(x)