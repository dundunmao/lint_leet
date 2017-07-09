class Solution:
    # @param {character[][]} grid Given a 2D grid, each cell is either 'W', 'E' or '0'
    # @return {int} an integer, the maximum enemies you can kill using one bomb
    def maxKilledEnemies(self, grid):
        # Write your code here
        m, n = len(grid), 0
        if m:
            n = len(grid[0])
        result, rows = 0, 0
        cols = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rows += 1

                if i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            cols[j] += 1

                if grid[i][j] == '0' and rows + cols[j] > result:
                    result = rows + cols[j]

        return result

class Solution1:
    # @param {character[][]} grid Given a 2D grid, each cell is either 'W', 'E' or '0'
    # @return {int} an integer, the maximum enemies you can kill using one bomb
    def maxKilledEnemies(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        score = [[0 for i in range(n+2)] for j in range(m+2)]
        for i in range(0,m):
            row = [0 for _ in range(n+2)]
            for j in range(1,n+1):
                if grid[i][j-1] == 'W':
                    continue
                elif grid[i][j-1] == 'E':
                    row[j] = row[j-1] + 1
                elif grid[i][j-1] == '0':
                    row[j] = row[j-1]
                    score[i+1][j] = score[i+1][j]+ row[j]
            row = [0 for _ in range(n + 2)]
            for j in range(n,0,-1):
                if grid[i][j-1] == 'W':
                    continue
                elif grid[i][j-1] == 'E':
                    row[j] = row[j+1] + 1
                elif grid[i][j-1] == '0':
                    row[j] = row[j+1]
                    score[i+1][j] += row[j]


        for j in range(0, n):
            col = [0 for _ in range(m + 2)]
            for i in range(1, m + 1):
                if grid[i-1][j] == 'W':
                    continue
                elif grid[i-1][j] == 'E':
                    col[i] = col[i - 1] + 1
                elif grid[i -1][j] == '0':
                    col[i] = col[i - 1]
                    score[i][j+1] = score[i][j+1] + col[i]


            col = [0 for _ in range(m + 2)]
            for i in range(m, 0, -1):
                if grid[i - 1][j] == 'W':
                    continue
                elif grid[i - 1][j] == 'E':
                    col[i] = col[i + 1] + 1
                elif grid[i - 1][j] == '0':
                    col[i] = col[i + 1]
                    score[i][j + 1] = score[i][j + 1] + col[i]
        result = 0
        for i in range(len(score)):
            for j in range(len(score[0])):
                result = max(result,score[i][j])
        return result
if __name__ == "__main__":
    s = Solution1()
    A = [['0', 'E', '0', '0'],
         ['E', '0', 'W', 'E'],
         ['0', 'E', '0', '0']]
    A = [['W', '0', '0', '0', '0', '0', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', '0', '0', '0', '0', '0', '0', 'W', 'W', 'W', '0', 'W', 'W', 'W', '0', '0', 'W', '0', 'W', '0', 'W', 'E', 'E', 'E', 'E', '0', '0', '0', '0', 'E', 'W', '0', '0', 'W']]
    print s.maxKilledEnemies(A)

