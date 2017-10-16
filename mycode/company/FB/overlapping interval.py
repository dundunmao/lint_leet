def overlap_interval(A):
    A = sorted(A,key = lambda x:x[0])
    for i in range(1,len(A)):
        if A[i][0]<A[i-1][1]:
            return False
    return True


if __name__ == '__main__':
    A = [(1,3), (0,3), (4,10), (50,51), (7,6)]
    print overlap_interval(A)