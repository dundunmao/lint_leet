# -*- encoding: utf-8 -*-
# 题目:n为version,这个version是坏的,说明前面就已经坏了,找到最开始坏的那个
# 标签:binary search
# 思路:用两个指针,front和back,看如果mid是True,说明还有往前走,所以新的back=mid-1.vice verse
#  The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        back = n-1
        front = 0
        while(front<=back):
            mid = (back+front)/2
            if isBadVersion(mid)==False:
                front = mid+1
            else:
                back = mid-1
        return front