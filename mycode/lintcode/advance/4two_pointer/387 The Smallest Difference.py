# -*- encoding: utf-8 -*-
# 题目: 给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。
# 样例: 给定数组 A = [3,4,6,7]， B = [2,3,8,9]，返回 0。
# 思路:本质是二路归并的思想,归成一路后,相邻两个的差值最接近.找最小.
class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
    def smallestDifference(self, A, B):
        if A is None or len(A) == 0 or B is None or len(B) == 0:
            return 0
        A.sort()
        B.sort()
        ai,bi = 0,0
        mini = float('inf')
        while ai < len(A) and bi < len(B):
            mini = min(mini, abs(A[ai] - B[bi]))
            if A[ai] < B[bi]:
                ai += 1
            else:
                bi += 1
        return mini
if __name__ == "__main__":
    s = Solution()
    A =[3,4,6,7]
    B =[2,3,8,9]
    print s.smallestDifference(A, B)