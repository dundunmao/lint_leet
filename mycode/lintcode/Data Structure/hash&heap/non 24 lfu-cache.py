# coding:utf-8
#  LFU是一个著名的缓存算法
# 实现LFU中的set 和 get
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# capacity = 3
#
# set(2,2)
# set(1,1)
# get(2)
# >> 2
# get(1)
# >> 1
# get(2)
# >> 2
# set(3,3)
# set(4,4)
# get(3)
# >> -1
# get(2)
# >> 2
# get(1)
# >> 1
# get(4)
# >> 4