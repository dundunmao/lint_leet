# -*- encoding: utf-8 -*-
# 题目；There is a fence with n posts, each post can be painted with one of the k colors. You have to paint all the posts such that no more than two adjacent fence posts have the same color. Return the total number of ways you can paint the fence.
# 刷n个栅栏，k种颜色，最多两个相邻的标杆能够颜色相同。问多少种方法。
# 第一栏:K种,
# 第二栏:如果一样就是k种(称之为same),如果不一样就是(k-1)种(称之为diff)
# 第三栏:对于二栏same,只能配k-1种不一样的(same*(k-1)),对于二栏diff,可以配一样的(diff*1)和不一样的(diff*(k-1))
# 所以这个时候diff*1就是same, same*(k-1)+diff*(k-1)就是diff
# 这个题跟198的rob题很像


def numWays(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n == 0: return 0
    if n == 1: return k

    # for the first 2 posts
    sameColor = k
    diffColor = k * (k - 1)

    for i in range(2, n):
        temp = diffColor
        diffColor = (sameColor + diffColor) * (k - 1)
        sameColor = temp

    return sameColor + diffColor

if __name__ == '__main__':
    n = 6
    k = 3
    print numWays(n, k)
