# -*- encoding: utf-8 -*-
# 1级
# 题目：给一个数组和一个目标int,要其中两个数之和等于这个目标int
# 思路：用dictionary。把每个数和目标数的差作为key,如果哪个数就是key，就可要返回值了。

def twoSum(num, target):
    d = {}
    for i in range(len(num)):
        if num[i] in d.keys():
            return (d[num[i]]+1, i+1)
        else:
            d[target - num[i]] = i

if __name__ == "__main__":
    num = [2, 7, 11, 15]
    target = 9
    print twoSum(num, target)


#_____________________________________

def add_sum(list_input, target):
    # # validate the list_input
    # if type(list_input) != 'list':
    #     return "input must be a list."
    # check edge case
    if list_input == []:
        return None

    dic = {}
    for i in range(0, len(list_input)):
        dic[target-list_input[i]] = i
    # print dic

    for i in range(0, len(list_input)):
        if dic.has_key(list_input[i]):
            index1 = dic.get(list_input[i])
            index2 = i

    return "index1 = "+str(index1), "index2 = "+ str(index2)

if __name__ == '__main__':
    # #case1: illegel case
    # print add_sum(12, 9) == "input must be a list."

    #case2: edge case
    print add_sum([], 9) == None
    # case 3: normal case1:
    print add_sum([2, 7, 11, 15], 9)
    # case 4: normal case2:
    print add_sum([4, 7, 11, 0], 11)

