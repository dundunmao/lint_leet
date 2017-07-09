# -*- encoding: utf-8 -*-
# 题目；抢劫房子,list里的数为房子里的钱,连着的房子不能抢,问最多能抢多少钱.
# 思路：其实就是在某个数组里面找一个序列， 序列里面的每一个元素都不能相邻，然后求其最大和
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )

# DP
# rob_house[i] = max(rob_house_i, not_rob_house_i)
#              = max(house[i] + rob_house[i-2], rob_house[i-1])
def rob(nums):
    # validate check
    if type(nums) is not list:
        return 'please input a list'
    # empty list
    if len(nums) == 0:
        return 0
    # f_0 = nums[0]
    # f_1 = max(nums[0], nums[1])
    # f_2 = max(f_0 +nums[2],f_1)
    # f_3 = max(f_1 +nums[3],f_2)
    if len(nums) == 0:
        return 0,None
    if len(nums) == 1:
        return nums[0],[0]
    if len(nums) == 2:
        result_list = nums.index(max(nums[0], nums[1]))
        return  max(nums[0], nums[1]),result_list

    f_pre_pre = nums[0]
    result_list_pre_pre = [0]
    f_pre = max(nums[0], nums[1])
    result_list_pre = [nums.index(max(nums[0], nums[1]))]
    f_now = 0
    result_list = []
    for i in range(2,len(nums)):
        if f_pre_pre+nums[i] >= f_pre:
            f_now = f_pre_pre+nums[i]
            result_list = result_list_pre_pre + [i]
        else:
            f_now = f_pre
            result_list = result_list_pre
        f_pre_pre = f_pre
        result_list_pre_pre = result_list_pre
        f_pre = f_now
        result_list_pre = result_list
    return f_now,result_list

# DP2
def rob_dp(nums):
    # validate check
    if type(nums) is not list:
        return 'please input a list'

    if len(nums) == 0:
        return 0,None
    if len(nums) <3:
        return max(nums)
    pre_pre = 0 #代表当前要遍历的位置的前前个的总共sum
    pre = 0     #代表当前要遍历的位置的前一个的总共sum
    for i in nums:
        mid = pre                   #记录下更新前的pre值
        pre = max(pre_pre + i, pre)  #更新pre
        pre_pre = mid               #更新pre_pre
    return pre


# recursive

def _rob(nums,i):
    if i == 2:
        return max(nums[1],nums[0])
    if i == 1:
        return nums[0]
    if i == 0:
        return 0
    return max(_rob(nums[0:i-1],i-1), _rob(nums[0:i-2],i-2)+nums[i-1])

def result(nums):
    # validate check
    if type(nums) is not list:
        return 'please input a list'
    i = len(nums)
    return _rob(nums,i)

def result_list(nums):
    i = len(nums)
    if i == 2:
        return [nums.index(max(nums[0], nums[1]))]
    if i == 1:
        return [0]
    if i == 0:
        return 0, None
    if _rob(nums[0:i-1],i-1) >=_rob(nums[0:i-2],i-2)+nums[i-1]:
        return result_list(nums[:i-1])
    else:
        return result_list(nums[:i-2])+[i-1]







if __name__ == '__main__':
    #testing
    # case 1:  illegal input such as a dictionary
    nums = {}
    print rob(nums)
    print result(nums)
    # case 2: edge case, empty list
    nums = []
    print rob(nums)
    print result(nums)
    # case 3: normal input 1
    nums = [5,4,17,19]
    print rob_dp(nums)
    # print result(nums),result_list(nums)
    # # # case 4: normal input 2
    # nums = [5,4,17,19,3]
    # print rob(nums)
    # print result(nums),result_list(nums)
    # # case 5: edge case only 3 house
    # nums = [1,1,1]
    # print rob(nums)
    # print result(nums),result_list(nums)


