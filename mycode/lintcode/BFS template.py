# -*- encoding: utf-8 -*-
# bfs的模板,并且带level order的
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
from Queue import Queue
def BFS_level_order(root):
    result = []  #为level准备的
    if root is None:
        return result
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        level = []
        size = queue.qsize()
        for i in range(size):
            head = queue.get()
            level.append(head.val)
            if head.left is not None:
                queue.put(head.left)
            if head.right is not None:
                queue.put(head.right)
        result.append(level)
    return result


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