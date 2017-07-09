# -*- encoding: utf-8 -*-
# 1级
# 内容:input:[[1,1],2,[1,1]] output:[1,1,2,1,1]; input[1,[4,[6]]]  output[1,4,6]
# 主要方法:
# http://demo.netfoucs.com/l294265421/article/details/51203616#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """


    def next(self):
        """
        :rtype: int
        """


    def hasNext(self):
        """
        :rtype: bool
        """
        # if there is no list in that list

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())