# -*- encoding: utf-8 -*-
# 题目；抢劫房子,list里的数为房子里的钱,连着的房子不能抢,问最多能抢多少钱.这回房子排成binary tree。就是他个他的父节点及左右子节点不能同时。

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#DF DFS
class Solution(object):
    def rob(self, root):
        rob_root, not_rob_root = self.dfs(root)
        return max(rob_root, not_rob_root)

    def dfs(self, node):
        if node is None:
            return (0, 0)
        rob_left, not_rob_left = self.dfs(node.left)
        rob_right, not_rob_right = self.dfs(node.right)

        rob_node = node.val + not_rob_left + not_rob_right
        not_rob_node = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        # Think about it: Why not "not_rob_node = rob_left + rob_right"?

        return (rob_node, not_rob_node)



#RECURSIVE DFS
class Solution1(object):
    def rob(self, root):
        return self.robDFS(root)[1]
    def robDFS(self,node):
        if node is None:
            return (0,0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))

if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
     #          26
     #        /   \
     #      10     3
     #    /    \     \
     #  4      6      3
    P = Node(26)
    P.left = Node(10)
    P.left.left = Node(4)
    P.left.right = Node(6)
    P.right = Node(3)
    P.right.right = Node(3)
    s = Solution()
    print s.rob(P)