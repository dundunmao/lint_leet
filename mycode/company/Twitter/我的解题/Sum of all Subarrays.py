# -*- encoding: utf-8 -*-
# Given an integer array ‘arr[]’ of size n, find sum of all sub-arrays of given array.
#
# Examples:
#
# Input   : arr[] = {1, 2, 3}
# Output  : 20
# Explanation : {1} + {2} + {3} + {2 + 3} +
#               {1 + 2} + {1 + 2 + 3} = 20
#
# Input  : arr[] = {1, 2, 3, 4}
# Output : 50
# 方法一：two pointer
def sum_subarray(arr):
    res = []
    array = []
    ans = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            array = arr[i:j]
            print array
            ans += sum(array)
    return ans
# 方法二：数学归纳

# Every element arr[i] appears in two types of subsets:
# i)  In sybarrays beginning with arr[i]. There are
#     (n-i) such subsets. For example [2] appears
#     in [2] and [2, 3].
# ii) In (n-i)*i subarrays where this element is not
#     first element. For example [2] appears in
#     [1, 2] and [1, 2, 3].
#
# Total of above (i) and (ii) = (n-i) + (n-i)*i
#                             = (n-i)(i+1)

def sum_subarray1(arr):
    res = 0
    for i in range(len(arr)):
        res += (arr[i] * (i + 1) * (len(arr) - i))
    return res

if __name__ == "__main__":
    arr = [1,2,3,4]
    print sum_subarray(arr)
