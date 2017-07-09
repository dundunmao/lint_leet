import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def __init__(self):
        self.num_of_ele = 0
        self.min_heap = []
        self.max_heap = []
    def medianII(self, nums):
        result = []
        for j in range(0, len(nums)):
            self.add_num(nums[j])
            result.append(self.get_med())
        return result

    def add_num(self, value):
        heapq.heappush(self.max_heap,-value)
        if self.num_of_ele % 2 == 0:
            if len(self.min_heap) == 0:
                self.num_of_ele += 1
                return
            elif -self.max_heap[0] > self.min_heap[0]:
                max_heap_root = -heapq.heappop(self.max_heap)
                min_heap_root = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_heap_root)
                heapq.heappush(self.min_heap, max_heap_root)
        else:
            heapq.heappush(self.min_heap, (-heapq.heappop(self.max_heap)))
        self.num_of_ele += 1

    def get_med(self):
        return -self.max_heap[0]

if __name__ == '__main__':
    s = Solution()

    # a =[1, 2, 3, 4, 5]   #return [1, 1, 2, 2, 3]
    a = [4, 5, 1, 3, 2, 6, 0]   #return [4, 4, 4, 3, 3, 3, 3]
    print s.medianII(a)
