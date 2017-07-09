# coding:utf-8
# 3级
# 题目:给一个非负整数list,从index=0开始,每个element代表你这一跳最多可以跳几步,问你能不能跳到最后一个index上
# 例如A = [2,3,1,1,4], return true; A = [3,2,1,0,4], return false
# 贪婪算法

# Going forwards. m tells the maximum index we can reach so far.
def canJump(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:               #如果遍历到i,但是最大步走不到这,就失败
            return False
        m = max(m, i+n)         #遍历到index=i时,最多能走到哪.max(m, i+n)其中m是之前那些步最多能走到哪,i+n是第i步最多能走到哪
    return True

# Going backwards
def canJump1(nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:     #这一步加上这一步最多能走的步,能达到下一步,就是goal
            goal = i                #那goal就为这一步的index. 如果达不到下一步,那goal不变,往前遍历,看看前面有没有能达到的.
    return not goal

if __name__ == '__main__':
    nums = [3,2,1,0,4]
    canJump1(nums)