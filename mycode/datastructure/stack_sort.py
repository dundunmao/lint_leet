__author__ = 'eva'
from stack import Stack

def stack_sort(list_check):
    if len(list_check) <= 1:
        return list_check
    s1 = Stack(len(list_check))
    s2 = Stack(len(list_check))
    for i in range(1,len(list_check)):
        if list_check[i] < list_check[0]:
            s1.push(list_check[i])
        else:
            s2.push(list_check[i])

    list1 = []
    list2 = []



    return s1,s2






if __name__ == "__main__":
    list_check = [18,1,10,100,50,2,200,100]
    print stack_sort(list_check)