# -*- encoding: utf-8 -*-
# 内容：找出list里出现重复出现一半以上的元素
# 思路：存在dictionary里。主意，取长度时用float，这样除以2时才是浮点数。

def majorityElement( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in range(0, len(nums)):
        if dic.has_key(nums[i]):
            dic[nums[i]] += 1
            if dic[nums[i]] >=(float(len(nums))/2):   #如果对应的value比长度的一般大
                return nums[i]
        else:
            dic[nums[i]] = 1

#求重复次数最多的那个值,放进dictionary里后,给diction的(key,value)排序
def majorityElement1(nums):
    d = {}
    for i in range(len(nums)):
        if d.has_key(nums[i]):
            d[nums[i]]+=1
        else:
            d[nums[i]] = 1
    print d
    result = [(key,value) for (key,value) in sorted(d.items(),reverse=True)]
    return result[0][0]

if __name__ == "__main__":
    nums = [5,6,6]

    print majorityElement(nums)