# -*- encoding: utf-8 -*-
class HashHeap:
    def __init__(self,mod):
        self.heap = []
        self.hash = {}  # item = (val,(id,count)) 此题里val是高度,id是在heap里的id,count(记录有几个有此高度的的点)
        self.size_t = 0
        self.mode = mod
    def peek(self):
        return self.heap[0]
    def size(self):
        return self.size_t
    def is_empty(self):
        return len(self.heap) == 0
    def parent(self,id):
        if id == 0:  #如果id=0,就没有parent
            return -1
        return (id - 1) / 2  #parent id
    def lson(self, id):
        return id * 2 + 1
    def rson(self, id):
        return id * 2 + 2
    def compare(self,a,b):
        if a <= b:   #如果a小于b,mode应该是min
            if self.mode == 'min':
                return True
            else:
                return False
        else:        #如果a大于b,mode应该是max
            if self.mode == "min":
                return False
            else:
                return True


    def swap(self, a, b):
        val_a = self.heap[a]   #heap里node上的值
        val_b = self.heap[b]
        count_a = self.hash[val_a][1]   #这个值(val)在hash里对应的那个(id,count)里的count
        count_b = self.hash[val_b][1]
        self.hash[val_b] = (a, count_b)  #在hash里把id对换了
        self.hash[val_a] = (b, count_a)
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a] #在heap里把值对换了.

    def poll(self):
        self.size_t -= 1
        now = self.heap[0]  #root的值
        hash_now = self.hash[now]  #现在的hash的item
        if hash_now[1] == 1:     #如果这个height只出现过一次
            self.swap(0,(len(self.heap) - 1))  #把root跟最后一个leaf交换
            del self.hash[now]        #在hash里删掉root对应的item
            del self.heap[len(self.heap) - 1]  #在heap里删掉交换后的那个leaf
            if len(self.heap) > 0:
                self.shiftdown(0)
        else:          #如果这个height出现过多次,就把count-1
            self.hash[now] = (0,hash_now[1] - 1)
        return now


    def add(self, now):   #这里now是height
        self.size_t += 1
        if self.hash.has_key(now): #如果hash里面存过这个height,在hash里别的不变,count+=1,heap不变
            hash_now = self.hash[now]   #[id, count]
            self.hash[now] = (hash_now[0],hash_now[1] + 1)
        else:                     #如果hash里没存过这个height,hash加入这个,heap也加入这个在最后的位置上
            self.heap.append(now)
            self.hash[now] = (len(self.heap) - 1, 1)
            self.shiftup(len(self.heap) - 1) #在heap里把最后一个node向上调整

    def delete(self, now):  #now就是height
        self.size_t -= 1
        hash_now = self.hash[now] #[id, count]
        if hash_now[1] == 1:   #如果 这个height只出现过一次,
            self.swap(hash_now[0],len(self.heap)-1)  #把它跟最后那个位置交换,
            del self.hash[now]  # 在hash里删掉height对应的item
            del self.heap[len(self.heap) - 1]  # 在heap里删掉调换后的最后那个node
            if len(self.heap) > hash_now[0]:
                self.shiftup(hash_now[0])
                self.shiftdown(hash_now[0])
        else:
            self.hash[now] = (hash_now[0], hash_now[1] - 1)

    def shiftup(self, id): #此节点往上调整
        while self.parent(id) > -1:#如果有父节点
            parent_id = self.parent(id)
            if self.compare(self.heap[parent_id], self.heap[id]):  #父节点上的value比此节点value大,就什么都不做
                break
            else:   #父比子小,就交换
                self.swap(parent_id,id)
            id = parent_id

    def shiftdown(self, id): #此节点往下调整
        while self.lson(id) < len(self.heap): #如果有左孩子
            left_id = self.lson(id)
            right_id = self.rson(id)
            if right_id >= len(self.heap) or self.compare(self.heap[left_id], self.heap[right_id]):#如果没有右孩子或左孩子大于右孩子
                son = left_id #左孩子为那个要交换的node
            else:
                son = right_id #否则就是右孩子为要交换的node
            if self.compare(self.heap[id], self.heap[son]): #如果此node比要交换的那个node大,就什么也不做
                break
            else:
                self.swap(id,son) #否则就交换
            id = son

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if len(nums) == 0:
            return []
        ans = []
        median = nums[0]
        max_heap = HashHeap('max')
        min_heap = HashHeap('min')
        for j in range(0,len(nums)):
            if j != 0:
                if nums[j] > median:
                    min_heap.add(nums[j])
                else:
                    max_heap.add(nums[j])
            if j >= k:
                if median == nums[j - k]:
                    if max_heap.size() > 0:
                        median = max_heap.poll()
                    elif min_heap.size() > 0:
                        median = min_heap.poll()
                elif median < nums[j - k]:
                    min_heap.delete(nums[j - k])
                else:
                    max_heap.delete(nums[j - k])
            while max_heap.size() > min_heap.size():
                min_heap.add(median)
                median = max_heap.poll()
            while min_heap.size() > max_heap.size() + 1:
                max_heap.add(median)
                median = min_heap.poll()
            if j + 1 >= k:
                ans.append(median)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,7,8,5]  # ans = [2,7,7]
    k = 3
    print s.medianSlidingWindow(nums, k)
