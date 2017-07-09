# coding:utf-8
# 3级
# 题目:array里有三个颜色,让同色的挨一起.可以用0,1,2代替三个颜色(不许用sort build-in)

def sortColors(A):
    if len(A)==0:
        return
    start=0
    end=len(A)-1
    cur=start
    while cur<=end and cur<len(A):
        if A[cur]==0:      #如果A[cur]=0,让他跟start互换,然后cur和start都往下走
            A[cur]=A[start]
            A[start]=0
            start+=1
            cur+=1
        elif A[cur]==1:     #如果A[cur]=1,cur接着往下走.
            cur+=1
        elif A[cur]==2:     #如果A[cur]=2,让他跟end换,然后end往回走.
            A[cur]=A[end]
            A[end]=2
            end-=1

#用了quick sort的方法
def sortColors1(nums):
    i = j = 0
    for k in xrange(len(nums)):  # k往下遍历
        v = nums[k]
        nums[k] = 2        #先让遍历到的数变成2,如果已经是2,这轮就结束,如果不是往下看.
        if v < 2:          #每次遍历到1或者0时,i这个地方就变成1,并且往下走一个.如果是1,往下走一个是为1挪出一个位置.如果是0也往下走,是为0也腾出个位置.
            nums[j] = 1
            j += 1
        if v == 0:         #每次遍历到1,j这个地方就变成1,并且往下走一个.
            nums[i] = 0
            i += 1
    return nums

#我的解法.不对,不要用remove,会变长度
def sortColors2(nums):
    for i in range(0,len(nums)):
        if nums[i]  == 0:
            a = nums[i]
            nums.remove(nums[i])
            nums.insert(0,a)

        elif nums[i] == 2:
            b = nums[i]
            nums.remove(nums[i])
            nums.append(b)
        else:
            continue
    return nums
if __name__ == '__main__':
    nums =[2,1,0,1,2,1,0,1,2]
    print sortColors1(nums)