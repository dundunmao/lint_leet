# coding:utf-8
# 合并两个排序的整数数组A和B变成一个新的数组。
#
#  注意事项
#
# 你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 A = [1, 2, 3, empty, empty], B = [4, 5]
#
# 合并之后 A 将变成 [1,2,3,4,5]
class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if A is None and B is None:
            return None
        if A is None:
            return None
        if B is None:
            return A
        i = m-1
        j = n-1
        k = 1
        while i>=0 and j>=0:
            if A[i] < B[j]:
                A[-k] = B[j]
                j -=1
            else:
                A[-k] = A[i]
                i -= 1
            k += 1
        while i>= 0:
            A[-k] = A[i]
            i -= 1
            k += 1
        while j>= 0:
            A[-k] = B[j]
            j -= 1
            k += 1

        return A[:n+m]

if __name__ == "__main__":

    A = [1,2,3,0,0]
    B = [4,5]
    m = 3
    n = 2
    s = Solution()

    print s.mergeSortedArray( A, m, B, n)
