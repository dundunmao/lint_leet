# coding:utf-8

# 3级
# 题目:有个高度数组，就相当于隔板的高度，求数组中任意两隔板间盛水的最大量。隔板间的距离与较低隔板的高度乘积即为盛水的容量。第块隔板的高度为ai
class Solution:
    # @return an integer
    def maxArea(self, height):
        left,right=0,len(height)-1
        maxi=(right-left)*min(height[left],height[right])  # maxi为left和right间的最大容积
        while left+1<right:
            if height[left]>height[right]:          #如果left比right高
                right-=1                            #right就往前走一个
                if height[right]>height[right+1]:   #如果新right比旧right高
                    maxi=max(maxi,(right-left)*min(height[left],height[right])) #maxi等于刚才的maxi和现在的maxi里最大的那个
            else:                                   #如果left比right矮
                left+=1                             #left就往后走一个
                if height[left]>height[left-1]:     #如果新left比旧left高
                    maxi=max(maxi,(right-left)*min(height[left],height[right])) #maxi等于刚才的maxi和现在的maxi里最大的那个
        return maxi