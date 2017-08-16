# -*- encoding: utf-8 -*-
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees,
# you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
#     4
# Therefore, you need to return above trees' root in the form of a list.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 建一个hash，duplicate的tree的前序遍历就是key,它的根就是value
class Solution(object):

    def findDuplicateSubtrees(self, root):
        hash = collections.defaultdict(list)  #dict表示成每个value都是一个list，同一个key的value都append到里面
        self.tuplify(root,hash)               #把duplicate的subtree都放同一个key的value里
        return [roots[0] for roots in hash.values() if roots[1:]] #如果value里有两个以上的node，他就是要要找的

    # 存hash,key为一个tuple,里面存了树的前序遍历（根左右）结构，既（根，左，右）value存的是root这个node。
    # 例子中的hash如下：
    # {(1, (2, (4, None, None), None), (3, (2, (4, None, None), None), (4, None, None))): [ node_1],
    #  (3, (2, (4, None, None), None), (4, None, None)): [ node_3],
    #  (4, None, None): [ node_4,node_4,node_4],
    #  (2, (4, None, None), None): [ node_2,node_2]
    #  }
    def tuplify(self,root,hash):
        if root:
            tuple = (root.val, self.tuplify(root.left,hash), self.tuplify(root.right,hash))
            hash[tuple].append(root) #如果是同一个tuple，就是同一个value，左右子树的
            return tuple
        else:
            return None

class Solution1(object):
    def findDuplicateSubtrees(self, root):
        res = []
        hash = {}
        self.helper(root, hash, res)
        return res
    def helper(self,cur,hash,res):
        if cur is None:
            return '#'
        serial = str(cur.val) + ',' + self.helper(cur.left,hash,res)+','+self.helper(cur.right,hash,res)
        if hash.setdefault(serial,0) == 1:
            res.append(cur)
        hash[serial] = hash.setdefault(serial,0) + 1
        return serial
if __name__ == "__main__":
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4

    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.right = TreeNode(3)
    P.right.right = TreeNode(4)
    P.right.left = TreeNode(2)
    P.right.left.left = TreeNode(4)
    Q = TreeNode(1)
    R = None
    s = Solution1()
    h = {}
    # print s.tuplify(R,h)
    print s.findDuplicateSubtrees(P)