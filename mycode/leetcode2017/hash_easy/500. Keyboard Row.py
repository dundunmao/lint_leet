# -*- encoding: utf-8 -*-
# 给一组词，问里面哪些词在键盘的同一行里
# 例子：input=["Hello","Alaska","Dad","Peace"]，output = ['Alaska', 'Dad']
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        f = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        s = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        t = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for w in words:
            w_low = w.lower()
            l = w_low[0]
            flag = True
            if l in f:
                for i in range(1, len(w)):
                    if w[i] not in f:
                        flag = False
                        break
                if flag == False:
                    continue
                ans.append(w)

            elif l in s:
                for i in range(1, len(w)):
                    if w[i] not in s:
                        flag = False
                        break
                if flag == False:
                    continue
                ans.append(w)
            elif l in t:
                for i in range(1, len(w)):
                    if w[i] not in t:
                        flag = False
                        break
                if flag == False:
                    continue
                ans.append(w)
        return ans

class Solution_leet(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans = []
        for word in words:
            t = set(word.lower())  #take set because it doesn't matter how many times the element appears
            if t & a == t:  #word和键盘某一排取交集==word，
                ans.append(word)
            if t & b == t:
                ans.append(word)
            if t & c == t:
                ans.append(word)
        return ans
if __name__ == "__main__":
    nums = ["Hello","Alaska","Dad","Peace"]
    x = Solution()
    print x.findWords(nums)