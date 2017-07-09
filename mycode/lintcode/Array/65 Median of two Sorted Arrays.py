# -*- encoding: utf-8 -*-
# 两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组A = [1,2,3,4,5,6] B = [2,3,4,5]，中位数3.5
#
# 给出数组A = [1,2,3] B = [4,5]，中位数 3

# 我的练习，建了一个新array，往里面不断的填数，最后填到中位数那个位置，取值。
class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        if A is None or B is None:
            return None
        i = 0
        j = 0
        new = []
        if len(A) == 0:
            new = B
        elif len(B) == 0:
            new = A
        else:

            while i< len(A) and j < len(B):
                if A[i] <= B[j]:
                    new.append(A[i])
                    i +=1
                else:
                    new.append(B[j])
                    j += 1
            if i < len(A):
                new.extend(A[i:])
            elif j < len(B):
                new.extend(B[j:])
        if (len(A)+len(B))%2 != 0:
            return new[(len(A)+len(B))/2]
        else:
            return (new[(len(A)+len(B))/2]+ new[(len(A)+len(B))/2-1])/2.0


class Solution_optimal(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            first = self.findKthElement(nums1, 0, m - 1, nums2, 0, n - 1,(m + n) // 2)
            second = self.findKthElement(nums1, 0, m - 1, nums2, 0, n - 1,(m + n) // 2 + 1)
            return (first + second) / 2.0
        else:
            return self.findKthElement(nums1, 0, m - 1, nums2, 0, n - 1,(m + n) // 2 + 1)
    def findKthElement(self, nums1, s1, e1, nums2, s2, e2, k):
        # 短的在前面
        if e1 - s1 > e2 - s2:
            return self.findKthElement(nums2, s2, e2, nums1, s1, e1, k)
        # 前面的array空了，直接去后面的第K个
        if s1 > e1:
            return nums2[s2 + k - 1]
        # k 为1时，两个队列还都没空时，取两个队列的最小
        if k == 1:
            return min(nums1[s1], nums2[s2])
        # 两个队列都取k的一半
        # a 为k的一半，如果k的一半比前面的array还长，就去前面array的总长
        a = min(k // 2, e1 - s1 + 1)
        # b 为k里剩下那些，大部分情况也是k的一半
        b = k - a
        # 如果 k一半那个数两个队列是一样的，说明他就是第k个数
        if nums1[s1 + a - 1] == nums2[s2 + b - 1]:
            return nums1[s1 + a - 1]
        # 如果前面队列里k一半那个数<后面队列里k一半那个数，就把前面队列前k/2扔掉
        elif nums1[s1 + a - 1] < nums2[s2 + b - 1]:
            return self.findKthElement(nums1, s1 + a, e1, nums2, s2, e2, k - a)
        else:
            return self.findKthElement(nums1, s1, e1, nums2, s2 + b, e2, k - b)


if __name__ == "__main__":

    A = [1,2,3,4,5,6]
    B = [2,3,4,5]
    s = Solution()

    print s.findMedianSortedArrays( A, B)