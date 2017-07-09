__author__ = 'eva'

def bubbleSort(li):

    for j in range(0,len(li)-1):
        for i in range(0,len(li)-1):
            if li[i] > li[i+1]:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
            i += 1
        j += 1
    return li

def insertSort(li):
    for i in range(1, len(li)):
        if i == 1:
            temp1 = li[i-1]
            if li[i] > li[i-1]:
                li[i-1] = temp1
            else:
                li[i-1] = li[i]
                li[i] = temp1
            continue
        temp2 = li[i]
        for j in range(0, i):

            if li[i-1-j]>temp2:
                li[i-1-j+1] = li[i-1-j]
                li[i-1-j] = temp2
    return li


def selectSort(li):

    for i in range(0, len(li)):
        temp = li[len(li)-i-1]
        maxi = max(li[0:len(li)-i])
        li[len(li)-i-1] = maxi
        li[li.index(maxi)] = temp
    return li



def quickSort(li):


    return li

# def mergeSort(li):
#
#
#     for i in range(0,len(li),2):
#         if i == len(li)-1:
#             break
#         temp1 = li[i]
#         temp2 = li[i+1]
#
#         if li[i] > li[i+1]:
#             li[i] = temp2
#             li[i+1] = temp1
#         else:
#             li[i] = temp1
#             li[i+1] = temp2
#
#     for j in range(1,len(li)/2*j):
#         if j == 1:
#             for i in range(0,len(li),2*j):
#                 if i == len(li)-1:
#                     break
#                 temp1 = li[i]
#                 temp2 = li[i+1]
#
#                 if li[i] > li[i+1]:
#                     li[i] = temp2
#                     li[i+1] = temp1
#                 else:
#                     li[i] = temp1
#         else:
#             li1 = []
#             for i in range(0,len(li),2*j):
#
#     return li


def eleven_1(l1,l2):
    l3 = l1+l2
    return selectSort(l3)
def a(li):
    print len(li)
    # for i in range(0,len(li)):
    #     print i
    mid=int(len(li)/2)
    print mid
    print li[:mid]
    print li[mid:]
if __name__ == "__main__":
    L1 = [22,1,2,30,40,50,60]
    L2 = [3,12,34,44,55]
    L3 = [5,3,14,20,7,5,10,1,22,6,8]
    L3 = [5,3,  14,20,  7,5, 10,1, 22,6, 8]
    # print bubbleSort(L3)
    # print insertSort(L3)
    # print selectSort(L3)
    # print eleven_1(L1,L2)
    #print mergeSort(L3)
    a(L1)