def min_max_1(A,lo,hi):
    if lo == hi:
        return A[lo],A[hi]
    p = partition(A, lo, hi)
    if p == lo:
        l_mini, l_maxi = A[lo], A[lo]

    else:
        l_mini, l_maxi = min_max_1(A, lo, p - 1)
    if p == hi:
        r_mini, r_maxi = A[hi],A[hi]
    else:
        r_mini,r_maxi= min_max_1(A,p+1,hi)
    return l_mini,r_maxi


def partition(A, lo, hi):
    i = lo
    j = i
    while j < hi+1:
        if A[j] <= A[hi]:
            A[i],A[j] = A[j],A[i]
            i += 1
            j += 1
        else:
            j += 1
    return i-1
if __name__ == "__main__":

    # a = [2,5,10,3,8,1,4,100]
    a = [1,1,1,1,2,2,2]
    print min_max_1(a,0,len(a)-1)


def min_max(A,lo,hi):
    if hi == lo:
        return A[lo],A[lo]
    l_mini,l_maxi = min_max(A,lo,lo+(hi-lo)/2)
    r_mini,r_maxi= min_max(A,lo+(hi-lo)/2+1,hi)
    return min(l_mini,r_mini), max(l_maxi,r_maxi)

def majority(A):
    le = len(A)
    left = helper(A)
    if left != [] and A.count(left[0]) > le/2:
            return left[0]
    else:
        return None
def helper(A):
    le = len(A)
    if le == 2:
        if A[0] != A[1]:
            return []
        else:
            return A
    if le == 1:
        return A
    left = helper(A[:le/2+1])
    right = helper(A[le/2+1:])
    if len(left) == len(right):
        if left == [] or left[0] != right[0]:
            return []
        else:
            return left+right
    else:
        i = 0
        j = 0
        while i < len(left) and j< len(right):
            if left[i] != right[j]:
                del left[i]
                del right[j]
            else:
                break
        return left + right



# if __name__ == "__main__":
#
#     a = [1,1,1,1,2,2,2]
#
#     print majority(a)