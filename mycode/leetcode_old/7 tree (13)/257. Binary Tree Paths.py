# -*- encoding: utf-8 -*-
# 标签：Tree Depth-first Search
# 题目；Given a binary tree, return all root-to-leaf paths.
#    1
#  /   \
# 2     3   to ["1->2->5", "1->3"]
#  \
#   5
# 思路：三种方法：深度遍历，广度遍历，recursive。
import collections
# dfs + stack
def binaryTreePaths1(self, root):  #往stack里压节点，左，右，再POP右，并把右的左右分别压进去，再pop最后面的，直到最后面的没有左右了。
    if not root:
        return []
    res = []
    stack = [(root, "")]   #双引号+string就是把string扩在双引号里。
    while stack:
        node, ls = stack.pop()   #ls是记录路径的，开始是“”，后来一点点往里填路径。所以这道题的关键是往ls里存所有的东西
        if not node.left and not node.right:    #如果是叶子，就只返回点的值
            res.append(ls+str(node.val))    #之前的路径+最后叶子的值
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res

# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res

# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res
def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
    if root.left:
        self.dfs(root.left, ls+str(root.val)+"->", res)
    if root.right:
        self.dfs(root.right, ls+str(root.val)+"->", res)