# -*- encoding: utf-8 -*-
# 给出一个非负整数数组，你最初定位在数组的第一个位置。　　　
#
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　
#
# 判断你是否能到达数组的最后一个位置。
#
#  注意事项
#
# 这个问题有两个方法，一个是贪心和 动态规划。
#
# 贪心方法时间复杂度为O（N）。
#
# 动态规划方法的时间复杂度为为O（n^2）。
#
# 我们手动设置小型数据集，使大家阔以通过测试的两种方式。这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# A = [2,3,1,1,4]，返回 true.
#
# A = [3,2,1,0,4]，返回 false.
# DP
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        can = [False for i in range(len(A))]
        can[0] = True
        for i in range(1,len(A)):
            for j in range(0,i):
                if can[j] and j+A[j]>=i:
                    can[i] = True
                    break
        return can[-1]
class Solution_greedy:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False] * n
        f[0] = True
        for i in range(0, n):
            if f[i] == True:
                for j in range(1, A[i] + 1):
                    if i + j <= n - 1:
                        f[i + j] = True
                    else:
                        break
        return f[n - 1]

# greedy method 我的练习
class Solution3:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False for i in range(n)]
        f[0] = True
        for i in range(0, n):
            if f[i] == True:
                for j in range(1, A[i] + 1):
                    if i + j < n:
                        f[i + j] = True
            else:
                return False
        return f[-1]


if __name__ == '__main__':
    s = Solution5()
    x = [4,6,9,5,9,3,0]
    print s.canJump(x)