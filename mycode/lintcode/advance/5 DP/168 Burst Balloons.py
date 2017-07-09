# -*- encoding: utf-8 -*-
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        n = len(nums)
        f = [[0 for i in range(n + 2)] for j in range(n + 2)]
        visit = [[0 for i in range(n + 2)] for j in range(n + 2)]
        nums.append(1)
        nums.insert(0,1)
        return self.search(nums,f,visit,1,n)
    def search(self,arr,f,visit,left,right):
        if visit[left][right] == 1:
            return f[left][right]
        res = 0
        for k in range(left,right+1):
            mid_value = arr[left-1]*arr[k]*arr[right+1]
            left_value = self.search(arr,f,visit,left,k-1)
            right_value = self.search(arr,f,visit,k+1,right)
            res = max(res,left_value+mid_value+right_value)
        visit[left][right] = 1
        f[left][right] = res
        return res
if __name__ == "__main__":
    s = Solution()
    A = [4,1,5,10]
    print s.maxCoins(A)