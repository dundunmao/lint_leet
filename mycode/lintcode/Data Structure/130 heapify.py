class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range((len(A) - 1) / 2, -1, -1):
            self.siftdown(A, i)
        return A
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            left = k * 2 + 1
            right = k * 2 + 2
            next = k
            if right < len(A) and A[left] > A[right]:
                next = right
            if A[next] >= A[k]:
                break
            A[next], A[k] = A[k], A[next]
            k = next
class Solution1:
    # @param A: Given an integer array
    # @return: void
    def heapify(self,A):
        size = len(A) - 1
        for i in range(size/2,-1,-1):
            self.helper(A,i)
        return A
    def helper(self, A,i):
        size = len(A) - 1
        l = i * 2 + 1
        r = l+1
        largest = i
        if l <= size and A[l] < A[i]:
            largest = l
        if r <= size and A[r] < A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] =A[largest], A[i]
            self.helper(A,largest)

if __name__ == '__main__':
    n = [3,2,1,4,5,7,9]
    s = Solution1()
    print s.heapify(n)