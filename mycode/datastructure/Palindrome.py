__author__ = 'eva'

def Palindrome (list1):
    # list2 = list1
    # list1.reverse()

    list2 = []
    for i in range(len(list1)):
        list2.append(list1[len(list1)-i-1])

    for i in range(len(list1)):

        for j in range(len(list1)):
            if j <= i+2:
                continue
            list1_sub = list1[i:j]
            for k in range(len(list2)):
                list2_sub = list2[k:k+len(list1_sub)]
                if list2_sub == list1_sub:
                    return True
    return False

if __name__ == "__main__":
    list1 = [1,3,2,3,2,1,3,4]
    res = Palindrome (list1)
    print (res)