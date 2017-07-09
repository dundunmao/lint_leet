# coding:utf-8
# 3级
# 题目: Given a singly linked list L: L0→L1→…→Ln-1→Ln,reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…in-place(分半,然后后面的反向插入前面的)
# For example:Given {1,2,3,4}, reorder it to {1,4,2,3}.
# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves

class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if not head or not head.next:
            return

        a, b = self._splitList(head)  #从中间断开
        b = self._reverseList(b)      #把后面那个翻转
        head = self._mergeLists(a, b) #把两个merge

    def _splitList(self,head):
        fast = head
        slow = head
        while fast and fast.next:  #slow走一步,fast走两步
            slow = slow.next
            fast = fast.next
            fast = fast.next
        middle = slow.next     #middle为后面的头
        slow.next = None      #断开
        return head, middle

    def _reverseList(self,head):
        last = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next #指定current的下一个那个node叫next
            currentNode.next = last     #current的next指向last
            last = currentNode          #current那个位置定义为last
            currentNode = nextNode      #next那个位置定义为current
        return last

    def _mergeLists(self,a, b):
        tail = a
        head = a
        a = a.next
        while b:
            tail.next = b   #head一直保持在那,a和b每一轮后都完后走并且互换,这样tail不断的指b,再指a
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head