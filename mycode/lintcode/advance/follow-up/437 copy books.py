# -*- encoding: utf-8 -*-
# 二分
class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        if len(pages) == 0:
            return 0
        total = 0
        maxi = pages[0]
        for i in range(0, len(pages)):
            total += pages[i]
            maxi = max(maxi,pages[i])
        start = maxi
        end = total
        while start + 1 < end:
            mid = start + (end - start)/2
            if self.helper(pages, mid) > k:
                start = mid
            else:
                end = mid
        if self.helper(pages,start) <= k:
            return start
        return end

    def helper(self,pages, limit):
        if len(pages) == 0:
            return 0
        copiers = 1
        sum = pages[0]
        for i in range(1, len(pages)):
            if sum + pages[i] > limit:
                copiers += 1
                sum = 0
            sum += pages[i]
        return copiers


   # DP
class Solution1:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        n = len(pages)
        if (k>n): k = n
        if n == 0:
            return 0
        sum = [0 for _ in range(n)]
        sum[0] = pages[0]
        for i in range(1, n):
            sum[i] = sum[i-1]+pages[i]
        f = [[0 for _ in range(k)] for _ in range(n)]
        for i in xrange(n):
            f[i][0] = sum[i]
        for j in xrange(1, k):
            p = 0
            f[0][j] = pages[0]
            for i in xrange(1, j):
                f[i][j] = max(f[i-1][j], pages[i])
            for i in xrange(j, n):
                while (p<i and f[p][j-1]<sum[i]-sum[p]):
                    p += 1
                f[i][j] = max(f[p][j-1], sum[i]-sum[p])
                if (p>0):
                    p -= 1
                f[i][j] = min(f[i][j], max(f[p][j-1], sum[i]-sum[p]))
        return f[n-1][k-1]
if __name__ == "__main__":
    s = Solution1()
    A = [3,2,4,6,7]
    k = 3
    print s.copyBooks(A,k)