
# -*- encoding: utf-8 -*-
# 在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 1->3->2->null，给它排序变成 1->2->3->null.
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        if head is None:
            return None
        return self.quick_sort(head)
# check duplicate
    def is_duplicat(self, head):
        while head is not None:
            if head.next is not None and head.next.val != head.val:
                return False
            head = head.next
        return True
# partition
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
        head_new = self.partition(head, head.val)
        cur = head_new
        dummy = ListNode(0)
        dummy.next = head_new
        pre = dummy
        while cur is not None:
            if cur.val == head.val:
                break
            cur = cur.next
            pre = pre.next
        pre.next = None
        left = dummy.next
        right = cur.next
        cur.next = None

        left = self.quick_sort(left)
        right = self.quick_sort(right)

        if left is not None:
            dummy.next = left
            while left.next is not None:
                left = left.next
            left.next = cur
        else:
            dummy.next = cur
        cur.next = right
        return dummy.next


# 我的练习之quick-sort
class Solution1:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        if head is None:
            return None
        return self.quick_sort(head)

    def is_duplicat(self, head):
        while head is not None:
            if head.next is not None and head.next.val != head.val:
                return False
            head = head.next
        return True

    def partition(self, head):
        left = ListNode(0)
        dummy_left = left
        right = ListNode(0)
        dummy_right = right

        flag = head.val
        cur = head.next
        while cur is not None:
            if cur.val < head.val:
                left.next = cur
                left = left.next
                cur = cur.next
            else:
                right.next = cur
                right = right.next
                cur = cur.next
        right.next = None
        left.next = None
        return dummy_left.next, dummy_right.next, ListNode(flag)
    def quick_sort(self, head):
        if head is None or head.next is None:
            return head
        if self.is_duplicat(head):
            return head
        dummy = ListNode(0)
        dummy.next = head

        left,right,mid = self.partition(head)

        quick_left = self.quick_sort(left)
        quick_right = self.quick_sort(right)
        if quick_left is None:   #注意这里,要考虑如果左半部分是None时的情况
            dummy.next = mid
            mid.next = quick_right
        else:
            cur_left = quick_left
            while cur_left is not None and cur_left.next is not None:    #找到 左半部分的最后一个node
                cur_left = cur_left.next
            cur_left.next = mid
            mid.next = quick_right
            dummy.next = quick_left

        return dummy.next
# 我的练习之merge-sort
class Solution2:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        part1, part2 = self.get_two_parts(head)
        part1_sort = self.sortList(part1)
        part2_sort = self.sortList(part2)
        return self.merge(part1_sort,part2_sort)
    def merge(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1 is not None:    # 这地方注意,别忘了把剩下的接上
            cur.next = head1
        elif head2 is not None:
            cur.next = head2
        return dummy.next
    def get_two_parts(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None
        part1 = dummy.next
        return part1, part2
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next= ListNode(2)
    s = Solution2()
    #test def merge
    head1 = ListNode(3)
    head2 = ListNode(3)
    head2.next = ListNode(4)
    test = s.merge(head1,head2)
    a = s.sortList(head)
    x = a
    while x is not None:
        print x.val
        x = x.next
