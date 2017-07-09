# -*- encoding: utf-8 -*-
# bfs的模板
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# 1: traverse
def traverse(root):
    if root is None:
        return None
    traverse(root.left)
    traverse(root.right)

# 2: divid & conquer
def traversal(root):
    if root is None:
        return None
    left = traversal(root.left)
    right = traversal(root.right)

    result = merge(left, right)
    return result
def merge():
    return None
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          26
    #        /   \
    #      10     10
    #    /    \   /  \
    #  4      6   6   4
    # /                \
   # 3                  3
    P = Node(26)
    P.left = Node(10)
    P.left.left = Node(4)
    P.left.left.left = Node(3)
    P.left.right = Node(6)
    P.right = Node(10)
    P.right.right = Node(4)
    P.right.right.right = Node(3)
    P.right.left = Node(6)
    print BFS_level_order(P)