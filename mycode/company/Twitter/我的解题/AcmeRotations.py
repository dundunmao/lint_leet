# -*- encoding: utf-8 -*-
# Lexicographically minimal string rotation最小字典序
# 输入"bbaaccaadd" output "aaccaaddbb"

# 方法一：Booth's Algorithm
def least_rotation(S):
    S += S      # Concatenate string to it self to avoid modular arithmetic
    f = [-1] * len(S)     # Failure function
    k = 0       # Least rotation of string found so far
    for j in xrange(1,len(S)):
        sj = S[j]
        i = f[j-k-1]
        while i != -1 and sj != S[k+i+1]:
            if sj < S[k+i+1]:
                k = j-i-1
            i = f[i]
        if sj != S[k+i+1]: # if sj != S[k+i+1], then i == -1
            if sj < S[k]: # k+i+1 = k
                k = j
            f[j-k] = -1
        else:
            f[j-k] = i+1
    return k

# 方法二：The Naive Algorithm
def least_rotation1(S):
    if len(S) < 2:
        return 0
    count = 0
    compare = S
    rotate = S
    compare_count = 0
    while count != len(S):
        rotate = rotate[1:]+ rotate[0]
        count += 1
        if check(rotate,compare):
            compare = rotate
            compare_count = count
    return compare_count

def check(A,B):
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if ord(A[i]) < ord(B[j]):
            return True
        elif ord(A[i]) == ord(B[j]):
            i += 1
            j += 1
        else:
            return False
    if i < len(A):
        return False
    return True
if __name__ == "__main__":
    S ="bbaaccaadd"
    S = 'bbabcab'
    print check('ADCD','ABCD')
    print least_rotation(S)
