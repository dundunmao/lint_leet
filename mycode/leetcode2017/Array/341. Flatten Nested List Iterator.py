# -*- encoding: utf-8 -*-
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Given the list [[1,1],2,[1,1]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
#
# Example 2:
# Given the list [1,[4,[6]]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       if nestedList = NestedInteger()

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        print self.hasNext()

        nestedList, pos = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[pos].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            nestedList, pos = s[-1]  # pos 是遍历当前层的pointer，指向下一个要打印的ele
            if pos == len(nestedList):  # pos 越界时说明都打印完了，这一层的可以pop出去了
                s.pop()
            else:  # 如果没打印完，就开始
                x = nestedList[pos]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
if __name__ == '__main__':


    nestedList = [[1,1],2,[1,1],2]
    nestedList = NestedInteger()
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())