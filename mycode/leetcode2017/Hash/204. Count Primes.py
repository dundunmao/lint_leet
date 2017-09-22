# -*- encoding: utf-8 -*-
# N以内的质数有几个
#我的方法，Memory Limit Exceeded

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 0
        hash = []
        result = []
        for i in range(2,n):
            if i not in hash:
                result.append(i)
            for ele in result:
                if i*ele<n:
                    hash.append(i * ele)
        return len(result)


class Solution_leet(object):
    def countPrimes(self, n):
        array = [False for i in range(n)]
        count = 0
        for i in range(2,n):
            if array[i] == False:
                count += 1
                for j in range(2,n):
                    if i * j >= n:
                        break
                    array[i * j] = True
        return count

class Solution(object):
    def countPrimes1(self, n):
        if n<2:
            return 0
        array = [False for i in range(n)]
        i = 2
        while i < n:
            if array[i] == False:
                j = 2
                while i * j < n:
                    array[i*j] = True
                    j += 1
            i += 1
        count = 0
        for ele in array:
            if ele == False:
                count+=1
        return count - 2


#
if __name__ == "__main__":
    a = 499979
    a = 10
    x = Solution()
    print x.countPrimes1(a)