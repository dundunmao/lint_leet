# -*- coding: utf-8 -*-
# quick sort就是不断partition的过程
# 1．先从数列中取出一个数作为基准数。
# 2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
# 3．再对左右区间重复第二步，直到各区间只有一个数。
import random
def quick_sort(start, end, A):
    if start >= end:
        return
    left = start
    right = end
    pivot = A[(start+end)/2] # 找中间那个数,然后下面就是partition的过程
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right] > pivot:
            right -= 1
        if left <= right:
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
            left += 1
            right -= 1
    quick_sort(start, right, A)
    quick_sort(left, end, A)
    return A
if __name__ == '__main__':
    lst = []
    for i in range(30):
        lst.append(random.randint(1, 100))
    print lst
    result = quick_sort(0,29,lst)
    print result
