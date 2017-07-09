# -*- encoding: utf-8 -*-
# 2级
# 内容：list里，是否有相同数的index差不大于K的
# 思路：放dictionary里
# 主要方法:
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i in range(0,len(nums)):  #写入dict，element为key,index 为value
        if dic.has_key(nums[i]):
            dic.get(nums[i]).append(i)  #把dic里的一个value写成list背这个写法,
        else:
            dic[nums[i]] = [i]
    for value in dic.values():
        if len(value)>1:
            value.sort()
            diff = abs(value[0]-value[-1])
            if diff<k:
                return True
    return False


if __name__ =="__main__":
    nums = [1,2,3,4,2,1]
    k = 2
    print containsNearbyDuplicate(nums, k)