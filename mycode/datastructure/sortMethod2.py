__author__ = 'eva'

def mergesort(seq):
    if len(seq)<=1:
        return seq
    mid = int(len(seq)/2)
    left = mergesort(seq[:mid])
    right=mergesort(seq[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result


def qu_Sort_iter(li):
    for i in range(0,len(li)):
        if isinstance(li[i], basestring):
            print "pls input numbers"
        return

    if len(li)<=1:
        return li
    seq,k = qu_Sort(li)
    if len(li)<=2:
        return li
    mid = li[k]
    left = qu_Sort_iter(seq[:k])
    right = qu_Sort_iter(seq[k+1:])
    left.append(mid)
    return left+right

def qu_Sort(li):

    if len(li)==2:
        if li[0]>li[1]:
            p1 = li[0]
            li[0] = li[1]
            li[1] = p1
            return li,len(li)-1
        else:
            return li,len(li)-1
    if len(li) == 1:
        return li,len(li)-1

    i=0
    j=len(li)-2
    while i<len(li) and j<len(li):
        pivot = li[len(li)-1]
        while li[i]<pivot:
            i+=1
        while li[j]>=pivot and j>=0:
            j-=1
        if i >= j:
            p = li[i]
            li[i] = pivot
            li[len(li)-1] = p
            break
        a = li[i]
        b = li[j]
        li[j] = a
        li[i] = b

    return li,i


if __name__=='__main__':
    l1 = [44,44]
    l3 = ['d','b','c','a']
    l = [3,2,22,1,34,44,2,30]
    l2 = [4,4,3,2,3,3,4,5,8,1]
    #print(mergesort(seq))
    #print merge(l3,l2)
    #print qu_Sort(l2)
    print qu_Sort_iter(l3)
    # print qu_Sort(l1)
    # seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]
    # L1 = [22,1,2,30,40,50]
    # L2 = [3,12,34,44,2,55]
