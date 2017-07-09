# -*- encoding: utf-8 -*-
# 题目: 给定一组 n 个不同大小的 nuts 和 n 个不同大小的 bolts。nuts 和 bolts 一一匹配。 不允许将 nut 之间互相比较，
#   也不允许将 bolt 之间互相比较。也就是说，只许将 nut 与 bolt 进行比较， 或将 bolt 与 nut 进行比较。
#   请比较 nut 与 bolt 的大小。
# 样例:
# nuts = ['ab', 'bc', 'dd', 'gg'], bolts = ['AB', 'GG', 'DD', 'BC']
# 一组可能的返回结果是：
# nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG']

# class Comparator:
#     def cmp(self, a, b):
#         if a > b:
#             return  1
#         elif a == b:
#             return 0
#         else:
#             return -1
#         return
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        if nuts is None or bolts is None:
            return
        if len(nuts) != len(bolts):
            return
        self.qsort(nuts, bolts, 0, len(nuts) - 1,compare)
    def qsort(self, nuts, bolts, l, r,compare):
        if l >= r:
            return
        split_nut_pos = self.partition(nuts, bolts[l], l, r, compare)   #nuts上在l-r这段已经以bolts[l]这个值partition好了.
        split_bolt_pos = self.partition(bolts, nuts[split_nut_pos], l, r, compare)  #bolts上在l-r这段已经以nuts[split_nut_pos]这个值partition好了.
        #因为结果是一一对应的,所以partition的位置是一样的split_nut_pos=split_bolt_pos
        self.qsort(nuts, bolts, l, split_nut_pos - 1,compare)
        self.qsort(nuts, bolts, split_nut_pos + 1, r,compare)
    def partition(self, items, pivot, l, r, compare):
        if items == [] or pivot == None:
            return
        for i in range(l,r+1):
            if compare.cmp(pivot, items[i]) ==0 or compare.cmp(items[i], pivot) == 0:#如果只写一个会超时
                items[l],items[i] = items[i], items[l]
                break
        pivot_partner = items[l]
        while l < r:
            while l < r and (compare.cmp(pivot,items[r]) == -1 or compare.cmp(items[r],pivot) == 1): #在右边找到第一个比p小的
                r -= 1
            items[l] = items[r]                                                                     #给l赋值,l这个位置其实是空的;赋值完,r这个位置就空了
            while l < r and (compare.cmp(pivot,items[l]) == 1 or compare.cmp(items[l],pivot) == -1):#左边找到第一个比p小的
                l += 1
            items[r] = items[l]                                                                      # 给r赋值,r这个位置其实是空的;赋值完,l这个位置就空了
        #while跳出时,已经在l左的是比pivot_partner小的,在l右的是比pivot_partner大的.
        items[l] = pivot_partner #把pivot_partner按在空位
        return l
