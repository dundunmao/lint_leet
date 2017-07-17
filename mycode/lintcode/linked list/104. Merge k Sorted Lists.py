# -*- encoding: utf-8 -*-
# 合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null
# 三种方法 1:优先队列,2 recursive,3 两两合并
import heapq
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
# heap
    def mergeKLists1(self, lists):
        if not lists:
            return None
        ll = []
        for node in lists:
            if node:  #保证某一个node是None时不加入ll，因为None没有val
                ll.append((node.val, node))
        dummy = ListNode(-1)
        heapq.heapify(ll)
        cur = dummy
        while ll:
            small, node = heapq.heappop(ll)
            cur.next = node
            cur = node
            if node.next is None:
                continue
            heapq.heappush(ll,(node.next.val, node.next))
        return dummy.next

# divid & conquer
    def merge(self, list1, list2):
        dummy = ListNode(-1)
        cur = dummy
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if list1 is not None:
            cur.next = list1
        elif list2 is not None:
            cur.next = list2
        return dummy.next

    def mergeKLists(self, lists):

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)
# 2 by 2 merge
    def mergeKLists2(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return None
        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                if i+1>=len(lists):
                    break
                merge_list = self.merge(lists[i], lists[i+1])
                new_list.append(merge_list)
            if len(lists)%2 == 1:
                new_list.append(lists[len(lists) - 1])
            lists = new_list
        return lists[0]

import heapq
class Solution_self(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or len(lists) == 0:
            return []
        dummy = ListNode(-1)
        cur = dummy
        array = []
        for i in range(len(lists)):
            if lists[i] is not None:  #别忘啦这里防止
                array.append([lists[i].val,lists[i]])

        heapq.heapify(array)
        while array:
            va,li = heapq.heappop(array)
            cur.next = ListNode(va)
            cur = cur.next
            if li.next:
                li = li.next
                heapq.heappush(array,[li.val,li])
        return dummy.next
if __name__ == '__main__':

    # P = None
    #
    # O = ListNode(2)
    # O.next = ListNode(6)
    # O.next.next = ListNode(8)
    #
    # Q = ListNode(3)
    # Q.next = ListNode(4)
    # Q.next.next = ListNode(9)
    # lists = [O, P, Q]
    lists = [None]
    s = Solution()
    print s.mergeKLists1(lists)