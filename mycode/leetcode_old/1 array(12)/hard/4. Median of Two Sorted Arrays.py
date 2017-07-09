# -*- encoding: utf-8 -*-
# 3级
# 内容:两个sorted array,size m,n.求median中位数.时间复杂度O(log (m+n))
# 主要方法:


class Solution:
    # @return a float
    def findMedianSortedArrays(self, nums1, nums2):
        l=len(nums1)+len(nums2)
        return self.findKth(nums1,nums2,l//2) if l%2==1 else (self.findKth(nums1,nums2,l//2-1)+self.findKth(nums1,nums2,l//2))/2.0

    def findKth(self,nums1,nums2,k):    #找到两个合起来的第k个.
        if len(nums1)>len(nums2):       #让小的在前面,大的在后面,因为这个medium位置比小的size大.
            nums1,nums2=nums2,nums1
        if not nums1:                   #如果有一个不存在,那一定是小size那个不存在
            return nums2[k]
        if k==len(nums1)+len(nums2)-1:  #如果k为最大值,那就第k就是最大的那个
            return max(nums1[-1],nums2[-1])
        i=len(nums1)//2
        j=k-i
        if nums1[i]>nums2[j]: #如果i数>j数,说明可以把j之前的数都塞进i前面,j之后的数可能在i前,所以k应该在i以内,j以外.因为把j之前的数都排除了,所以就找k-j的那个数,就是
            return self.findKth(nums1[:i],nums2[j:],i)
        else:
            return self.findKth(nums1[i:],nums2[:j],j)

if __name__ =="__main__":
    nums1 = [1,3,5,6,10,11,12]
    nums2 = [7,8,9]
    s = Solution()
    print s.findMedianSortedArrays(nums1, nums2)