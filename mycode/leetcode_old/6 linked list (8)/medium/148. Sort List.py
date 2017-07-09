# coding:utf-8
# 3级
# 题目:Sort a linked list in O(n log n) time using constant space complexity.
# 思路:recursive
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# merge sort
class Solution(object):
    # merge sort, recursively
    def sortList(self, head):
        # nodes应该多余2个
        if head is None or head.next is None:
            return head
        # get mid node
        mid = self.mid(head)
        # cut the two list
        right_part = mid.next
        mid.next = None
        # sort the left & right
        right = self.sortList(right_part)
        left = self.sortList(head)
        # merge left & right
        return self.merge_sort(left, right)

    # merge sort for 2 lists
    def merge_sort(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next

    # get mid
    def mid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


# quick sort
class Solution2(object):
    # merge sort, recursively
    def sortList(self, head):
        if head is None:
            return None
        return self.quick_sort(head)

    # check duplicate,
    # 检查是不是这个list所有点都一个value
    def is_duplicat(self, head):
        while head is not None:
            if head.next is not None and head.next.val != head.val:
                return False
            head = head.next
        return True

    # partition
    # 用head.val做pivot,它前面的都比他小,后面的都没它小.
    def partition(self, head, x):
        if head is None:
            return None
        small = ListNode(0)
        dummy1 = small
        big = ListNode(0)
        dummy2 = big
        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
                head = head.next
            else:
                big.next = head
                big = big.next
                head = head.next
        big.next = None
        small.next = dummy2.next
        return dummy1.next

    # quick sort
    def quick_sort(self, head):
        if head is None:
            return None
        if self.is_duplicat(head):
            return head
        # 变成前一半比后一半小的list,head.val为pivot
        head_new = self.partition(head, head.val)
        # 排兵布阵,dummy,pre,cur都放上
        dummy = ListNode(0)
        dummy.next = head_new
        cur = head_new
        pre = dummy
        # 找到head.val,并以他为界,分为左右两部分
        while cur is not None:
            if cur.val == head.val:
                break
            cur = cur.next
            pre = pre.next
        # 在head.val前面断开
        pre.next = None
        # 分为三个部分:左,右,中
        # left
        left = dummy.next
        # right
        right = cur.next
        # cur(head.val) 单独一个点
        cur.next = None

        left = self.quick_sort(left)
        right = self.quick_sort(right)

        if left is not None:
            # dummy连接left
            dummy.next = left
            # 找到left的尾巴
            while left.next is not None:
                left = left.next
            # left的尾巴连接cur(head.val)
            left.next = cur
        else:
            dummy.next = cur
        # cur去连接 right
        cur.next = right
        return dummy.next


if __name__ == '__main__':
    P = ListNode(1)
    P.next = ListNode(-1)
    # P.next.next = Node(3)
    # P.next.next.next = Node(2)
    # P.next.next.next.next = Node(5)
    # P.next.next.next.next.next = Node(2)
    # P.next.next.next.next.next.next = Node(7)
    s = Solution2()
    print s.sortList(P)
