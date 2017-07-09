class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        # Write your code here
        result = [0,0]
        sum = 0
        n = len(A)
        start = 0
        end = 0
        local = 0
        glb = float('-inf')
        for i in range(0,n):
            sum += A[i]
            if local < 0:
                local = A[i]
                start = i
                end = i
            else:
                local += A[i]
                end = i
            if local >= glb:
                glb = local
                result = [start,end]
        local = 0
        start = 0
        end = -1
        for i in range(0,n):
            if local > 0:
                local = A[i]
                start = i
                end = i
            else:
                local += A[i]
                end = i
            if start == 0 and end == n - 1:
                continue
            if sum - local >= glb:
                glb = sum - local
                result = [(end+1)%n,(start-1+n)%n]
        return result
if __name__ == "__main__":
    s = Solution()
    A = [1,-1]
    print s.continuousSubarraySumII(A)
