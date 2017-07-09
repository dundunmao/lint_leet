class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        n = len(grid)
        m = len(grid[0])
        result = float('inf')
        if n == 0 or m == 0:
            return -1
        x = []
        y = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        total = len(x)
        x.sort()
        y.sort()
        sum_x = [0]
        sum_y = [0]
        for i in range(1,total+1):
            sum_x.append(sum_x[i - 1] + x[i - 1])
            sum_y.append(sum_y[i - 1] + y[i - 1])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cost_x = self.get_cost(x, sum_x, i, total)
                    cost_y = self.get_cost(y, sum_y, j, total)
                    result = min(result, cost_x+cost_y)
        return result

    def get_cost(self, x, sum, pos, n):
        if n == 0:
            return 0
        if x[0] > pos:
            return sum[n] - pos*n
        l = 0
        r = n-1
        while l+1<r:
            mid = l + (r-l)/2
            if x[mid] <= pos:
                l = mid
            else:
                r = mid-1
        index = 0
        if x[r] <= pos:
            index = r
        else:
            index = l
        return sum[n] - sum[index+1] - pos*(n-index-1)+(index+1)*pos - sum[index+1]

if __name__ == "__main__":
    s = Solution()
    A = [[0,1,0,0],[1,0,1,1],[0,1,0,0]]
    print s.shortestDistance(A)
