# -*- encoding: utf-8 -*-
# 题目 把"PAYPALISHIRING"写成
# P   A   H   N
# A P L S I I G
# Y   I   R
# 思路：划分块：cycle = (2*nRows - 2)，在每个circle里，除first和last行，其他行都是两个数。
# i是row,k是circle，j是第一竖趟的index，secondJ 是其他竖趟的index。
# j = i + cycle*k。secondJ = (j - i) + cycle - i。（j-i）就是circle的倍数。
def convert(s, numRows):
    if numRows<=1: return s
    cycle = numRows*2 - 2
    slen = len(s)
    res = ""
    for i in xrange(numRows):
        for j in xrange(i, slen, cycle):
            res += s[j]
            secondJ = (j - i) + cycle - i
            if (secondJ-j) % cycle != 0 and secondJ < slen:
                res += s[secondJ]
    return res


#我自己写的
def convert1(k, numRows):
    #check validate
    result_row = []
    N = len(numRows)//(2*k-2)+1

    for i in range(k):
        element = []
        # for j in range(N):
        j = 0
        while j< N:
            index=(2*k-2)*j
            # print index
            if i == 0:
                element.append(numRows[index])
            elif i == k-1:
                if index+i>=len(numRows):
                    break
                element.append(numRows[index+i])
            else:
                if index+i>=len(numRows):
                    break
                if index+k+1-i<len(numRows):
                    element.extend([numRows[index+i],numRows[index+k+1-i]])
                else:
                    element.append(numRows[index+i])

            j+=1
        # print element
        result_row.extend(element)
    return result_row

if __name__=='__main__':
    #case1: invalid input

    #case2: edge input

    #case3: nomal input
    numRows = 'PAYPALISHIRIN'
    k = 3
    print convert(k,numRows)
    print convert1(5,"123456789")