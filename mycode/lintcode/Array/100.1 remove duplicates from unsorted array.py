# -*- encoding: utf-8 -*-
# 给一个unsorted array, 返回无重复数的array,不包括重复的数
def removeDuplicates0(A):
    # edge case
    if A is None or len(A) == 0:
        return []
    # main part
    hash = {}
    result = []
    for i in range(len(A)):
        if hash.has_key(A[i]):
            hash[A[i]].append(i)
        else:
            hash[A[i]] = [i]
    for item in hash.items():
        if len(item[1]) == 1:
            result.append((item[0], item[1]))
    result = sorted(result, key=lambda x: x[1])
    return [x[0] for x in result]
if __name__ == "__main__":
    a = [1,2,2,2,2,5,4,4,4,3]
    # dict = ["a"]
    removeDuplicates0(a)