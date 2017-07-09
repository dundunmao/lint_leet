class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        le = len(digits)
        sum = 0
        for i in range(le):
            sum += digits[i] * 10 ** (le - 1 - i)
        sum += 1
        array = []
        s = str(sum)
        length = len(s)
        for i in range(length):
            array.append(int(s[i]))
        return array

