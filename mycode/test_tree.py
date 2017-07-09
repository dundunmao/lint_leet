# -*- encoding: utf-8 -*-
class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        list = []
        list.append(root)
        while list != []:
            l = len(list)
            list_level = []
            for i in range(l):
                if list[0].left:
                    list.append(list[0].left)
                if list[0].right:
                    list.append(list[0].right)
                top = list.pop(0)
                list_level.append(top.val)
            result.append(list_level)
        return result


if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
     #          26
     #        /   \
     #      10     3
     #    /    \     \
     #  4      6      3
    P = Node(10)
    P.left = Node(5)
    P.left.left = Node(4)
    P.left.right = Node(6)
    B = P.left.right
    B.parent = P.left
    P.left.parent = P
    P.right = Node(11)
    P.right.right = Node(12)
    A = P.right.right
    A.parent = P.right
    P.right.parent = P





    Q = Node(10)
    Q.left = Node(5)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    Q.right = Node(15)
    Q.right.left = Node(6)
    Q.right.right = Node(20)
    #
    s = Solution()
    print s.levelOrder(Q)
