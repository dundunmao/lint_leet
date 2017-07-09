# -*- encoding: utf-8 -*-
# 3级
# 题目：H篇文章被引用H遍以上。例如citations = [3, 0, 6, 1, 5]，有5篇文章,每篇文章被引用3,0,6,1,5遍
# 因为他有3篇文章被引用3遍以上,所以H=3
# 思路：先sort,[0,1,3,5,6],意思是:(5-0)篇被至少引用0次,(5-1)篇被至少引用1次,(5-2)篇被至少引用3次,(5-3)篇被至少引用5次,(5-4)篇被至少引用6次,
# 就是 citations[i] >= (n-i)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n-i):
                return n-i
        return 0