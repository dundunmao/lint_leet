
# -*- encoding: utf-8 -*-
# 1级
# 内容 移除list里的所有的val。（in place）
# 思路，用list.remove(val).len会变时，用while
#  not only the right answer of the list length is asked for, but also the right output list.
# So you have to do 'real' delete on the list and return the length of the new list.
# so this one is wrong
# 重点方法:
def removeElement(nums, val):
    while val in nums:  #这个跟for num in nums不一样.while这个需要已知val,for这个可以不知道num
        nums.remove(val)
    return len(nums)

def removeElement1(nums, val):
    nums = list(set(nums))
    nums.remove(val)
    return nums


#方法2
def removeElement2(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    num = []
    for i in nums:
        if i != val:
            num.append(i)
    nums[:len(num)] = num
    return len(nums)
#方法3
def removeElement3(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if not nums: return 0
    A = 0

    for num in nums:
        if num != val:
            nums[A] = num
            A += 1
    return A

#方法4
def remove(nums,val):

    if not nums:
        return 0
    i = 0
    j = len(nums)-1
    while i<j:
        if nums[j] == val:
            j-=1
            continue
        if nums[i] == val and nums[j]!=val:
            nums[i] = nums[j]
            nums[j] = val
            j -=1
        i +=1
    return len(nums[:j+1])


if __name__ =="__main__":
    nums = [7,8,9,7]
    val = 7
    print removeElement1(nums,val)
    print remove(nums,val)