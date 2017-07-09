# -*- encoding: utf-8 -*-
# 2级
# 题目:给定一个list的数字,每个element都出现两次,只有一个例外,找出来
# 思路:set的二倍-这个list的和

def singleNumber(A):
    return 2*sum(set(A))-sum(A)  # 1+3+5+2的二倍-sum

if __name__ == "__main__":
    A = [1,3,5,2,3,1,5]
    print singleNumber(A)