# coding:utf-8
# 2级
# 题目 一个list 和一个target,list是从小到大排序,是其中两个数加起来等于target,例如numbers={2, 7, 11, 15}, target=9.等到 index1=1, index2=2

def twoSum2(list,target):
    i = 0
    j = len(list)-1

    while i<len(list) and j<len(list):
        sum = list[i]+list[j]
        if sum>target:
            j-=1
        elif sum<target:
            i+=1
        else:
            return 'index1='+str(i)+' , '+'index2='+str(j)




if __name__ == '__main__':
    list = [2, 7, 11, 15]
    target = 9
    print twoSum2(list, target)