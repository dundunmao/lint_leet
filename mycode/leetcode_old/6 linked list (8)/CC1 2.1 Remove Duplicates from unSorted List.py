# -*- encoding: utf-8 -*-
# 2级
# （删除重复的node（unsorted的）
class Node(object):
    def __init__(self,data):
        self.val = data
        self.next = None
#  方法2:hashtable
def delete_duplicates1(head):
    dic = {}
    dic[head.val] = True
    node_pre = head         # The node right before the one under processing
    while node_pre.next != None:
        node_current = node_pre.next
        if dic.has_key(node_current.val):
            node_pre.next = node_current.next   # Delete the node
        else:
            dic[node_current.val] = True
            node_pre = node_current
    return head
if __name__ == '__main__':
    P = Node(1)
    P.next = Node(2)
    P.next.next = Node(3)
    P.next.next.next = Node(2)
    P.next.next.next.next = Node(5)
    P.next.next.next.next.next = Node(2)
    P.next.next.next.next.next.next = Node(7)
    delete_duplicates1(P)