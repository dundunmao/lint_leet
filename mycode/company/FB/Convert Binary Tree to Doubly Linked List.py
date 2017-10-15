class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class Solution:
    def __init__(self):
        self.root = Node(-1)
        self.head = Node(-1)
        self.prev = Node(-1)
    def BTtoDLL(self,root):
        if root is None:
            return
        self.BTtoDLL(root.left)
        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.BTtoDLL(root.right)
    def inorderTraversal(self, root):
        # write your code here
        if root == None:
            return []
        stack = []
        res = []
        cur = root
        while cur != None or stack != []:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur)
            cur = cur.right
        return res
    def DD(self,res):
        dummy = LinkNode(-1)
        dummy.next = res[0]
        res[0].prev = dummy



