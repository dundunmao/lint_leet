# -*- encoding: utf-8 -*-
# 给array of string['i', 'am', 'bob'],给一个上限长度k，这个为char的总共长度。为k能包含几个连续的string。
# input是 array of string,代表每个string的长度。和上线长度k。求string的各数。意思就是subarray sum <= k
def subarraySum(a,k):
    count = 0
    i = 0
    j = 1
    sum = a[i]
    while j < len(a) and i < j:
        if sum > k:
            sum -= a[i]
            i += 1
            if i == j:
                j += 1
        else:
            if count < j - i:
                count = j - i
            sum += a[j]
            j += 1


    return count


if __name__ == '__main__':
    s = [1,2,3]
    t =3

    print subarraySum(s,t)