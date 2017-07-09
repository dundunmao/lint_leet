# -*- encoding: utf-8 -*-
# 题目：Secret number:"1807";Friend's guess:"7810": 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# 思路：第一轮循环，用对应关系把bull找到，并且把secret里没被猜到的数作为dic里的key,value为+=1.
#      第二轮，遍历guess，里面的数，在dict的key里没有，就不是cow, 如果有，且对应的dict里的key的值>0,就说明是cows，cows的计数就+=1，然后value -=1

from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        digits = defaultdict(int)
        # first pass: count bulls and non-matching digits
        for index in range(len(secret)):  # 第一轮： 数 bulls 和 non-matching digits
            if secret[index] == guess[index]:
                # matches, count the number of bulls
                bulls += 1   # 如果match, 数 bulls的数量
            else:
                # not match, increase number of non-matching digits
                digits[secret[index]] += 1  # 如果不 match, increase number of non-matching digits

        # second pass: count number of cows
        for index in range(len(secret)):   # 第一轮: 数cows
            if secret[index] != guess[index]:
                # decrease number of non-matching digit by 1 if it is greater than 0
                if digits[guess[index]] > 0:  # 如果大于0，decrease number of non-matching digit
                    cows += 1
                    digits[guess[index]] -= 1

        return str(bulls) + 'A' + str(cows) + 'B'


if __name__ == "__main__":
    s = Solution()
    print s.getHint("1123","0111")