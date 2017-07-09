# coding:utf-8
# 3级
# 题目: 用插入排序sort一个linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution1:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        linkHead = ListNode(0)
        linkHead.next = head
        sortedEnd = linkHead.next

        if sortedEnd == None:
            return head

        while sortedEnd.next != None:
            pivot = sortedEnd.next                    #pivot指向尾巴的下一个,就是range外的第一个
            sortedEnd.next = pivot.next               #让尾巴和pivot的下一个相连

            pre = linkHead        #这个pre需要每次遍历都重新定位在头这,下面两个方法都是当pre比pivot大时才重新回到头那

            while pre != sortedEnd and pre.next.val < pivot.val: #当pre不是range里的最后一个点,而且pre的下一个的值比pivot值小时
                pre = pre.next                                     #pre成为他的下一个,也就是pre指向最后一个比pivot小的那个值

            pivot.next = pre.next   #把pivot插到pre后面,记住写法
            pre.next = pivot

            if pre == sortedEnd:               #如果pre为最后一个了
                sortedEnd = pivot                     #那pivot房子pre后面,pivot就成为最后一个

        return linkHead.next

class Solution2:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        linkHead = ListNode(0)
        linkHead.next = head
        sortedEnd = linkHead.next
        if sortedEnd == None:
            return head

        pre = linkHead.next  #declare pre here

        while sortedEnd.next != None:
            pivot = sortedEnd.next        #pivot在end的下一位
            sortedEnd.next = pivot.next   #end接上pivot的下一位
            # reset pre only when pivot is needed to be inserted before pre
            if pre.val > pivot.val:                                       #确定pre的位置
                pre = linkHead

            while pre != sortedEnd and pre.next.val < pivot.val:  #确定pre的位置
                pre = pre.next

            pivot.next = pre.next    #pivot插在pre后面
            pre.next = pivot

            if pre == sortedEnd:      #直到pre到最后了,pivot就变成最后一个点,这样就排好了
                sortedEnd = pivot

        return linkHead.next

#best solution
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        pre = end = dummy_head = ListNode(0)
        dummy_head.next = head

        while end.next:                       #end的下一位是pivot
            if pre.val > end.next.val:     #如果pre的值比end的下一位(pivot)值大
                pre = dummy_head                #pre就重新定位,pre定位在头那

            while pre.next.val < end.next.val:  #pre就往下走,直到他的下一个值比pivot大,那他现在就是最后一个比pivot小的值,pivot就应该插在他的下一位
                pre = pre.next

            if pre != end:                    #当pre不等于end时
                pivot = end.next                #end的下一位就是pivot
                end.next = pivot.next           #end连到pivot的下一位,就是让end跳过pivot跟他的下一位连上,把pivot挤出去
                pivot.next = pre.next           #pivot连到pre的下一位,把pre的后箭头断开
                pre.next = pivot                #pre的后箭头指向pivot-----.这样就完成了pivot的插入
            else:
                end = end.next                 #如果pre就是end,那end往下挪一位

        return dummy_head.next