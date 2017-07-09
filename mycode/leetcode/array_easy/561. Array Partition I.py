# -*- encoding: utf-8 -*-
# 题目：2n个数，凑n个pair使得 min(a1, b1),min (a2, b2), ...min(an, bn)的sum最大
# 例如：input=[1,4,3,2]，output=4.（ 4 = min(1, 2) + min(3, 4)）
# 解题：假设bi >= ai，所以Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn) =a1 + a2 + ... + an。此题要求这个Sm最大
#      di = bi - ai； Sd = d1 + d2 + ... + dn
#      Sa = a1 + b1 + a2 + b2 + ... + an + bn
# 所以 Sa = a1 +(a1 + d1)+ a2 +(a2 + d2)+ ... + an +(an + di) = 2Sm + Sd 即 Sm = (Sa - Sd) / 2
# 所以 Sa固定，要最大Sm就要找最小Sd。就是两个数间的距离的sum最小
# 没有overlap的间距和是最小的
# 所以就是（1，2）一组，（3，4）一组，（5，6）一组。取到的是1，3，5。。。他们的和。因为就是数组内奇数位的和

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result
