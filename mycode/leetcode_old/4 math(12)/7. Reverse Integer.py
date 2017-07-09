# -*- encoding: utf-8 -*-
# 标签：math
# 题目；把数字里的digit反过来。例:x = 123, return 321
# 思路：前按[1,2,3]存入list,再（（1*10）+2）*10+3
# class Solution:
# # @param {integer} x
# # @return {integer}
#     def reverse(self, x):
#         arr = []
#         f = False
#         if x < 0:
#             x *= -1
#             f = True
#         while True:
#             arr.append(x % 10)
#             x /= 10
#             if x == 0:
#                 break
#         result = 0
#         for i in arr:
#             result = i + 10 * result
#         if f:
#             result *= -1
#         return result
def reverse(x):
    result = 0
    lenx = len(str(x))
    for i in range(lenx):
        result += x%10*(10**(lenx-i-1))
        x = x//10
    return result
if __name__=='__main__':
    x = 123
    print reverse(x)