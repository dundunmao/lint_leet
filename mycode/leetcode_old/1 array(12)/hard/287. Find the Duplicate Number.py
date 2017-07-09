# -*- encoding: utf-8 -*-
# 3级
# 内容: n + 1 integers的list,where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
# Note:
# 1:You must not modify the array (assume the array is read only).
# 2:You must use only constant, O(1) extra space.
# 3:Your runtime complexity should be less than O(n2).
# 4:There is only one duplicate number in the array, but it could be repeated more than once.
#  主要方法: 鸽巢算法,如果有一个数(比如5)并且有5个数<=5,说明5往前都没duplicate,那那个duplicate一定>5.
class Solution(object):
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1    # n是多少
        mid = (high + low) / 2  # n/2
        while high - low > 1:
            count = 0        #记录 有多少个比大于n/2的数
            for k in nums:
                if mid < k <= high:
                    count += 1
            if count > high - mid:  #鸽巢算法,如果个数比后半段的size大,就是这些书都塞在后半段还有余,那duplicate一定在后半段.
                low = mid           #所以这里就取后半段
            else:
                high = mid
            mid = (high + low) / 2
        return high


if __name__ =="__main__":
    s = 'hello'
    print findDuplicate(s)