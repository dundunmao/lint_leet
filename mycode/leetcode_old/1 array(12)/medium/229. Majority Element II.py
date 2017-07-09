# -*- encoding: utf-8 -*-
# 3级
# 内容:n个element的list,找到所有出现了多余(n/3)次数的element,只能用o(1)space
#思路:Boyer-Moore Majority Vote algorithm(多数投票算法) 题169
#       1: 如果count==0，则将now的值设置为数组的当前元素，将count赋值为1；
#       2: 反之，如果now和现在数组元素值相同，则count++，反之count--；
#       3: 重复上述两步，直到扫描完数组。
#       4:求now这个值在数组里出现的次数,如果次数大于等于n/2，则返回now的值，反之则返回-1；
#而这道题,是要两个数符合条件:因为要多余n/3所以最多有两个符合条件
        # 就是数两个candidate的个数,遇到相同的就+1,不同的就-1这样相同和不相同互相抵消,最后留下的就是相同的个数多的

def majorityElement(nums):
# @param {integer[]} nums
# @return {integer[]}
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, -1
    for num in nums:
        if num == candidate1:  #当前遍历到的数跟candidate一样时,count自加1
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:  #count还没计数时,candidate=当前遍历到的数
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:               #count已经开始计数了,但是candidate跟当前的数不一样时,count自减1
            count1-=1
            count2-=1
    return [n for n in (candidate1, candidate2)    #求这两个candidate的次数大于n/3不.
                    if nums.count(n) > len(nums) // 3]

if __name__ =="__main__":
    nums = [1,2,3,4,1,2,1,2,1,2]
    print majorityElement(nums)