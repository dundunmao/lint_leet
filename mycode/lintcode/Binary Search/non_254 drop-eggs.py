# coding:utf-8
#  There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.
#
# You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor. But in this worst case (k = 10), you have to drop 10 times.
#
# Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst case (for example, k = 9) you have to drop 4 times.
#
# 样例
# Given n = 10, return 4.
# Given n = 100, return 14.