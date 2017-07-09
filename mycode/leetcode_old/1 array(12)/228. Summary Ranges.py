# -*- encoding: utf-8 -*-

#主要方法:
# 内容：list range连续性。given [0,1,2,4,5,7], return ["0->2","4->5","7"].
# 思路：一个函数用来显示箭头板式。另一个算数，用while。start标记一个开始，然后i+=1，遇到两个数差不等于1，把start和这个结尾输入板式。start从i+1开始进入下一轮
def summaryRanges(self, nums):
    if not nums:
        return []
    res, i, start = [], 0, 0
    while i < len(nums)-1:
        if nums[i]+1 != nums[i+1]:  #当相差不等于1时
            res.append(self.printRange(nums[start], nums[i]))   #写入板式。
            start = i+1
        i += 1
    res.append(self.printRange(nums[start], nums[i]))
    return res

def printRange(self, l, r):  #板式
    if l == r:
        return str(l)
    else:
        return str(l) + "->" + str(r)

#方法2:
# 用 while，i 不动时，j自加。pivot跟着j走。j会出界，这时候用except。list里只有一个数时单独论。
def summaryRanges(nums):
    list = []
    if len(nums)==1:
        return ["%d"%(nums[0])]
    if len(nums) == 0:
        return []
    i = 0
    j = 1
    p = nums[0]
    try:
        if j<len(nums):
            while i < len(nums):
                if nums[j]==p+1:
                    p = nums[j]
                    j+=1
                else:
                    if nums[i] == p:
                        list.append("%d"%(p))
                    else:
                        list.append("%d->%d"%(nums[i],p))
                    i = j
                    j = i+1
                    p = nums[i]
    except:
        if nums[i] == p:
            list.append("%d"%(p))
        else:
            list.append("%d->%d"%(nums[i],p))

    return list




if __name__ =="__main__":
    nums = [0,1,2,4,5,7]
    print summaryRanges(nums)
