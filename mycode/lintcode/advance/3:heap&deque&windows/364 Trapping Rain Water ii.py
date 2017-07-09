from heapq import heappush, heappop

class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        if heights == []:
            return 0

        m, n = len(heights), len(heights[0])
        visited = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        offsets = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]

        # Get the boundary.
        min_heap = [] # A priority queue
        for i in range(m):
            heappush(min_heap, (heights[i][0], i, 0))
            visited[i][0] = 1
            heappush(min_heap, (heights[i][n-1], i, n-1))
            visited[i][n-1] = 1
        for i in range(n):
            heappush(min_heap, (heights[0][i], 0, i))
            visited[0][i] = 1
            heappush(min_heap, (heights[m-1][i], m-1, i))
            visited[m-1][i] = 1

        # Start from the current shortest among the ones in the queue.
        # This ensures that a point would be explored from the LOWEST point around it!
        total_water = 0
        while min_heap:
            h, x, y = heappop(min_heap)
            for dx, dy in offsets:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    new_h = max(h, heights[new_x][new_y])
                    heappush(min_heap, (new_h, new_x, new_y))
                    if h > heights[new_x][new_y]:
                        total_water += h - heights[new_x][new_y]

        return total_water