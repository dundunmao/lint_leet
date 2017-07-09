# -*- encoding: utf-8 -*-
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        f = [0 for i in range(len(A)+1)]
        f[0] = 0
        f[1] = A[0]
        for i in range(2,len(A)+1):
            f[i] = max(f[i-1],f[i-2]+A[i-1])
        return f[len(A)]

#滚动数组优化
    def houseRobber1(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        f = [0,0]
        f[0] = 0
        f[1] = A[0]
        for i in range(2, len(A) + 1):
            f[i%2] = max(f[(i-1)%2], f[(i - 2)%2] + A[i - 1])
        return f[len(A)%2]
if __name__ == "__main__":
    s = Solution()
    A =[3]
    print s.houseRobber((A))