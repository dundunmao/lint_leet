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

# 
class Solution1(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        le = len(digits)
        sum = 0
        for i in range(le-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0,1)
        return digits
