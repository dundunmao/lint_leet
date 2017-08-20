# -*- encoding: utf-8 -*-
# 给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如果 A = [1, 2, 3], target = 2 and k = 3, 那么返回 [2, 1, 3].
#
# 如果 A = [1, 4, 6, 8], target = 3 and k = 3, 那么返回 [4, 1, 6].
class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Algorithm:
        # 1. Find the first index that A[index] >= target
        # 2. Set two pointers left = index - 1 and right = index
        # 3. Compare A[left] and A[right] to decide which pointer should move

        # Write your code here
        # edge case

        # intialize
        start = 0
        end = len(A) - 1
        index = -1
        result = []
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[start] >= target:
            index = start
        elif A[end] >= target:
            index = end
        else:
            index = end + 1
        left = index - 1
        right = index
        for i in range(k):
            if left < 0:   # 左边到头了
                result.append(A[right])
                right += 1
            elif right == len(A): #右边到头了
                result.append(A[left])
                left -= 1
            else:     #正常情况,左右比,谁小append谁
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
        return result


class Solution1(object):
    def kClosestNumbers(self, arr, x, k):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr == [] or arr is None or k == 0:
            return []

        s,e = self.binary(arr,x)
        res = []
        while s>= 0 and e<= len(arr) - 1:
            left = abs(arr[s] - x)
            right = abs(arr[e] - x)
            if left <= right:
                res.append([arr[s],left])
                if len(res) == k:
                    break
                s = s - 1
            elif left > right:
                res.append([arr[e],right])
                if len(res) == k:
                    break
                e = e + 1
        if s < 0 and len(res) < k:
            for i in range(k - len(res)):
                res.append([arr[e],abs(arr[e] - x)])
                e += 1
                if e > len(arr) - 1:
                    break
        elif e >= len(arr):
            for i in range(k - len(res)):
                res.append([arr[s], abs(arr[s] - x)])
                s -= 1
                if s < 0:
                    break
        for i in range(len(res)):
            if res[i][1] == res[i - 1][1] and res[i][0] < res[i-1][0]:
                res[i],res[i-1] = res[i-1],res[i]
        return [ele[0] for ele in res]
    def binary(self,arr,x):
        s = 0
        e = len(arr) - 1
        while s+1<e:
            m = s + (e-s)/2
            if x >= arr[m]:
                s = m
            else:
                e = m
        return s,e
if __name__ == "__main__":
    A =[1,10,15,25,35,45,50,59]
    target = 30
    k = 0
    s = Solution1()
    print s.kClosestNumbers(A, target, k)