# -*- encoding: utf-8 -*-
# Merge two given sorted integer array A and B into a new sorted integer array.
#
# Have you met this question in a real interview? Yes
# Example
# A=[1,2,3,4]
#
# B=[2,4,5,6]
#
# return [1,2,2,3,4,4,5,6]
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if A is None and B is None:
            return None
        if A is None:
            return B
        if B is None:
            return A

        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        if j >= len(B):
            result.extend(A[i:])
        if i >= len(A):
            result.extend(B[j:])
        return result
