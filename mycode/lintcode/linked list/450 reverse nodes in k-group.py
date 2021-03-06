# coding: utf-8
# 给你一个链表以及一个k,将这个链表从头指针开始每k个翻转一下。
# 链表元素个数不是k的倍数，最后剩余的不用翻转。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表 1->2->3->4->5
#
# k = 2, 返回 2->1->4->3->5
#
# k = 3, 返回 3->2->1->4->5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        dummy = ListNode(0)
        dummy.next = head
        pre_m = dummy
        # length
        length = self.length(head)
        times = length/k
        node_m = pre_m.next
        for j in range(times):
            # 每次定位node_n,post_n
            node_n = node_m
            post_n = node_n.next
            #片段翻转
            for i in range(1, k):
                # if post_n is None:node_m
                #     return None
                temp = post_n.next
                post_n.next = node_n
                node_n = post_n
                post_n = temp
            #头尾连上
            node_m.next = post_n
            pre_m.next = node_n
            #重新定位pre_m和node_m
            pre_m = node_m
            node_m = post_n
        # 打印检查
        # while dummy.next is not None:
        #     print dummy.next.val
        #     dummy = dummy.next
        return dummy.next

    def length(self, head):
        le = 0
        while head is not None:
            head = head.next
            le += 1
        return le


class Solution_leet(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        题：每k个数reverse一下，类似24Swap Nodes in Pairs每2个数reverse一下

        """
        curr = head
        count = 0;
        while curr != None and count != k:  # find the k+1 node
            curr = curr.next
            count += 1
        if count == k:  # if k+1 node is found
            curr = self.reverseKGroup(curr, k)  # reverse list with k+1 node as head
            # head - head-pointer to direct part,
            # curr - head-pointer to reversed part;
            while (count > 0):  # reverse current k-group:
                tmp = head.next  # tmp - next head in direct part
                head.next = curr  # preappending "direct" head to the reversed list
                curr = head  # move head of reversed part to a new node
                head = tmp  # move "direct" head to the next node in direct part
                count -= 1
            head = curr
        return head
if __name__ == "__main__":
    k = 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    s.reverseKGroup(head,k)