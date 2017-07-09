# -*- encoding: utf-8 -*-
# O(m + n)
class Solution:
    #@param A: An list of list integer
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        m = len(A)
        n = len(A[0])
        return self.helper(1,m-2,1,n-2,A,True)   #取四边以内的,True表示这里面有peak
    def helper(self,y1,y2,x1,x2,A,flag):
        if flag:
            mid = y1+(y2-y1)/2  #中间那行
            index = x1
            for i in range(x1,x2+1):
                if A[mid][i]> A[mid][index]:
                    index = i        #mid这行的最大值位置
            if A[mid-1][index] > A[mid][index]:
                return self.helper(y1,mid-1,x1,x2,A, not flag)
            elif A[mid+1][index] > A[mid][index]:
                return self.helper(mid+1, y2, x1, x2, A, not flag)
            else:
                return [mid,index] ####
        else:
            mid = x1+(x2-x1)/2
            index = y1
            for i in range(y1,y2+1):
                if A[i][mid]>A[index][mid]:
                    index = i
            if A[index][mid-1] > A[index][mid]:
                return self.helper(y1, y2, x1, mid-1, A, not flag)
            elif A[index][mid+1]>A[index][mid]:
                return self.helper(y1, y2, mid+1, x2, A, not flag)
            else:
                return [index,mid]

# o(nlog(n))
class Solution2:
    #@param A: An list of list integer
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        low = 1
        high = len(A)-2
        ans = []
        while low <= high:
            mid = (low+high)/2
            col = self.helper(mid, A) #找mid这一行最大值
            if A[mid][col] < A[mid-1][col]:#如果mid的上一行这个值更大,说明peak在上半块,把high放在mid这
                high = mid-1
            elif A[mid][col] < A[mid+1][col]:
                low = mid+1
            else:
                ans.append(mid)
                ans.append(col)
                break
        return ans
    def helper(self,row,A):
        col = 0
        for i in range(0, len(A[row])):
            if A[row][i] > A[row][col]:
                col = i
        return col