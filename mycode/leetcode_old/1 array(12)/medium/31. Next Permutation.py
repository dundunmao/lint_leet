# coding:utf-8

# 3级
# 题目:找到一组数字数列的下一个排序(按大小排的),就是找比当前数列大的下一个数
# 先把数列从右开始找到已经从大到小sorted的一部分,比如1342,其中42是已经按大到小排好的.所以就分成13,和42两部分.
# 然后把3用比他大的数替换掉,并且这个数要在后面这部分里.所以变成了14,32.然后再把32从小到大排序

def nextPermutation(nums):
    if(len(nums)<=1):return nums;
    else:
        # 找那个分界点
        splitIdx=-1
        for i in range(len(nums)-2,-1,-1): #倒着遍历,从倒数第二个遍历到头,(第一个-1就是头的意思,第二个-1是每次减1的意思)记住这个写法
            if(nums[i]<nums[i+1]): #找到第一个前面比后面小的数
                splitIdx=i         #返回这个数的位置
                break
        # 找能替换上的数
        replaceIdx=len(nums)-1
        while(replaceIdx > splitIdx):
            if(nums[replaceIdx]>nums[splitIdx]): #找那个比3大的数,并且这个数要在后面那块儿里
                break
            replaceIdx-=1

        nums[replaceIdx],nums[splitIdx]=nums[splitIdx],nums[replaceIdx]

        right=nums[splitIdx+1:]
        right=sorted(right)  #把后面那块sort了
        return nums[0:splitIdx+1]+right

if __name__ == '__main__':
    nums = [1,3,4,3,2,1]
    print nextPermutation(nums)