# coding:utf-8
# 3级
# 题目: Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
# 思路,跟list里那个题一样,一个fast一个slow往后遍历,他们的差就是那个断点.
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None

    if head.next == None:
        return head

    pointer = head
    length = 1

    while pointer.next:         #计算长度
        pointer = pointer.next
        length += 1

    rotateTimes = k%length      #计算slow和fast的差

    if k == 0 or rotateTimes == 0:
        return head

    fastPointer = head
    slowPointer = head

    for a in range (rotateTimes):   #fast先走
        fastPointer = fastPointer.next


    while fastPointer.next:         #fast,slow一起走,一直到fast走到头,这时候slow的位置就是断点
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next

    temp = slowPointer.next       #temp定位在slow的下一个,也就是新的头

    slowPointer.next = None        #slow的下一个变成空的
    fastPointer.next = head         #fast的下一个变成头
    head = temp                     #头变成temp

    return head