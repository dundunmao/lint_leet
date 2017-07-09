# -*- encoding: utf-8 -*-
# 给出一个非负整数数组，你最初定位在数组的第一个位置。
#
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)
class Solution:
    # @param A, a list of integers
    # @return an integer

    # greedy法
    def jump(self, A):
        p = [0]
        for i in range(len(A) - 1):
            while (i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        return p[-1]

    def jump(self, A):
        # write your code here
        f = [0 for i in range(len(A))]
        for i in range(1,len(A)):
            f[i] = float('inf')
            for j in range(0,i):
                if f[j] != float('inf') and j + A[j]>=i:
                    f[i] = f[j]+1
                    break
        return f[-1]


# 超时

class Solution1:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        n = len(A)
        f = [0 for i in range(n)]
        # step[0] = 0
        f[0] = 0
        for i in range(0, n):
            if A[i] != 0:
                for j in range(1, A[i] + 1):
                    if f[i + j] == 0:
                        f[i + j] = f[i] + 1
                    else:
                        f[i + j] = min(f[i + j], f[i] + 1)
                    if i + j == n-1:
                        return f[n - 1]
        return f[n - 1]

# 不对
class Solution5:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        n = len(A)
        f = [float('inf') for i in range(n)]
        f[0] = 0
        for i in range(0, n):
            if f[i] != float('inf'):
                for j in range(1, A[i] + 1):
                    if i + j < n:
                        f[i+j] = min(f[j], f[i] + 1)


        return f[-1]
# 对,但超时
class Solution4:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        n = len(A)
        f = [0 for i in range(n)]
        # f[0] = 1
        for i in range(1, n):
            for j in range(0, i):
                if j == 0 and A[j]>=i:
                    f[i] = 1
                    break
                if f[j] != 0 and j + A[j] >= i:
                    if f[i] == 0:
                        f[i] = f[j] + 1
                    else:
                        f[i] = min(f[i], f[j] + 1)
        return f[-1]




if __name__ == "__main__":
    # A = [2,3,1,1,4]
    A = [17,8,29,17,35,28,14,2,45,8,6,54,24,43,20,14,33,31,27,11]
    s = Solution4()
    print s.jump(A)