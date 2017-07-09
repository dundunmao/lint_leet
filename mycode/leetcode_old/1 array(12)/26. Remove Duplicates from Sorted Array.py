
# -*- encoding: utf-8 -*-
# 2级
# 内容：sorted list,移除重复的数。return长度
# 思路：i扫一遍，j在已经定下来的数的下一个等着,i遇到不重复的数x了,j那个位置就变成x,这个数就定下来了,
#       j往下去下一个数等着;i遇到重复的数就继续往下走,j不动..
#       这样i-j之间的距离就是所有重复的数的个数,j就是不重复的数的个数
#       j之前的element是所有不重复的element
#      意思就是往下扫,遇到跟前面数不一样的数,j的下一个数就变成这个数,把list里前面的数都变成不重复的数

#主要方法:

def remove(A):
# empty input
    if not A:
        return 0
#normal
    i = 1
    j = 1
    while i<len(A):       #这个方法是,i往下扫,遇到不重复的数(i-1跟的数不一样),就往j那放.最后符合条件的是j前面的那些数,所以长度就是j.
        if A[i-1] !=A[i]:
            A[j] = A[i]
            i+=1
            j+=1
        else:
            i+=1
    return j,A[0:j]

# 方法2:
#not sorted
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return []

    for i in range(0,len(nums)):
        if nums[i]=='r':
            continue
        for j in range(i+1,len(nums)):
            if nums[i]=='r':
                continue
            if nums[i] == nums[j]:
                nums[j] = 'r'

    while 'r' in nums:
        nums.remove('r')
    return nums


#sorted
#用remove会改变len。所以用try...except。因为移除一个元素后再下一层循环指针不想+1,所以用while，以及在while里制定j,k,
def removeDuplicates2(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    j=0
    k = 1
    try:
        while j<len(nums):
            if nums[j] == nums[k]:
                nums.remove(nums[k])
            else:
                j+=1
                k+=1
    except:
        return len(nums)




if __name__ =="__main__":
    # nums = [0,0,0,0]
    nums = [1,1,2,4,4,5,5,5,7]
    val = 5
    print remove(nums)