# coding:utf-8
# 3级
# 题目:remove 第二次 duplicated from sorted array,
# 例子:nums = [1,1,1,2,2,3],输出 nums= [1,1,2,2,3]
#思路: i<2就是不要考虑前两个数, 从第三个数开始:n > nums[i-2] 就是要现在现在轮到的数别他前面的前面大
#     如果大,就继续往下遍历,如果不大,i停在那,n往后走找到大的那个,替换

def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:  #i<2就是不要考虑前两个数, 从第三个数开始:n > nums[i-2] 就是要现在现在轮到的数别他前面的前面大,
            nums[i] = n
            i += 1
    return i

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates1(self, A):
        if len(A)==0:
            return 0
        cur=0
        point=0

        while point<len(A):
            if point<len(A)-2 and A[point]==A[point+1] and A[point]==A[point+2]: #符合条件,p就往下走,就是跳过一位的意思
                point=point+1
            else:
                A[cur]=A[point]                                     #不符合条件,就值替换,然后一起往下走
                point=point+1
                cur=cur+1
        return cur
if __name__ == '__main__':
    nums = [1,1,1,1,2,2,2,3,3,4]
    print removeDuplicates(nums)