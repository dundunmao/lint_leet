# -*- encoding: utf-8 -*-
# 给一个unsorted array, 返回无重复数的array,包括重复的数

def removeDuplicates( array):

    for i in range(len(array)):
        array[i] = (array[i], i)
    array.sort()
    j = 0
    for i in range(len(array)):
        if array[i][0] == array[i - 1][0]:
            i += 1
        else:
            array[j] = array[i]
            i += 1
            j += 1
    result = array[:j]
    result = sorted(result, key=lambda x: x[1])
    return [item[0] for item in result]
if __name__ == "__main__":
    a = [1,2,2,2,2,5,4,4,4,3]
    # dict = ["a"]
    print removeDuplicates(a)
