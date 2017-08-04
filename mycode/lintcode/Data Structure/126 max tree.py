# -*- encoding: utf-8 -*-

# 给出一个没有重复的整数数组，在此数组上建立最大树的定义如下：
#
# 根是数组中最大的数
# 左子树和右子树元素分别是被父节点元素切分开的子数组中的最大值
# 利用给定的数组构造最大树。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组 [2, 5, 6, 0, 3, 1]，构造的最大树如下：
#
#     6
#    / \
#   5   3
#  /   / \
# 2   0   1
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
#单调栈
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stack = []
        root = None
        for i in range(len(A)+1):
            if i == len(A):
                wait = TreeNode(float('inf'))
            else:
                wait = TreeNode(A[i])
            while len(stack) != 0 and wait.val > stack[-1].val:
                cur = stack.pop()
                if len(stack) == 0:
                    wait.left = cur
                else:
                    next = stack[-1]
                    if next.val > wait.val:
                        wait.left = cur
                    else:
                        next.right = cur
            stack.append(wait)
        return stack[-1].left

#用heap exceed time limite
import heapq
class Solution1:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        if len(A) == 0:
            return None
        h = []
        for i in range(len(A)):
            heapq.heappush(h,(-A[i],i))
        x,id = heapq.heappop(h)
        root = TreeNode(-x)
        root.left = self.maxTree(A[0:id])
        root.right = self.maxTree(A[id+1:len(A)])
        return root
if __name__ == '__main__':
    s = Solution1()

    A = [2, 5, 6, 0, 3, 1]
    print s.maxTree((A))
