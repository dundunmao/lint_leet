# -*- encoding: utf-8 -*-
# 1级
# 内容:n个element的list,是否有一个element出现了多余一半的次数(n/2)
#思路: 用dictionary

def majorityElement(nums):
    dic = {}
    for i in range(len(nums)):
        if dic.has_key(nums[i]):
            dic[nums[i]] +=1
            if dic[nums[i]]>len(nums)/2:
                return nums[i]

        else:
            dic[nums[i]] = 1

#Boyer-Moore Majority Vote algorithm(多数投票算法)
#       1: 如果count==0，则将now的值设置为数组的当前元素，将count赋值为1；
#       2: 反之，如果now和现在数组元素值相同，则count++，反之count--；
#       3: 重复上述两步，直到扫描完数组。
#       4:求now这个值在数组里出现的次数,如果次数大于等于n/2，则返回now的值，反之则返回-1；
# 总结就是:遍历,计数,如果相同就加1,如果不相同就减1.就是要相同的和不相同的互相抵消,最后剩下那个就是该找的
# ,只要是多余一半,那比如会有挨着的数是一样的情况,隔一个一样这种也是互相抵消的,不会记录下来
def majorityElement2(nums):
    count = 0
    candidate1 = 0
    for num in nums:    #找到挨着的一样的数,这个数出现的次数还大于一半
        if candidate1 == num:
            count +=1
        elif count == 0:
            candidate1 = num
            count +=1
        elif candidate1 != num:
            count-=1
    fre = nums.count(candidate1)
    if fre>len(nums)/2:
        return candidate1
    else:
        return -1
if __name__ =="__main__":
    nums = [1,4,4,4,2,2,2,2,2]
    print majorityElement2(nums)
