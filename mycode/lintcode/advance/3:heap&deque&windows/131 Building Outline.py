# -*- encoding: utf-8 -*-
# 用扫描线方法,取事件,每个building的位置,高度,左还是右.
# 排序
# 开始看每个点
# 如果是左:如果heap里是空的,或者比现在heap里最高的那个高,就加进来(说明新的building进来了,新的轮廓出来了,要记录这个起点)
# 如果是右,要先删除这个高度(这个高度未必是heap里的最大值):如果heap里空了,或者删除的这个高度比删除后heap里最大值要大,说明删除的这个是最大高度,说明删完轮廓高度变小,要记录这个落点
#     如果heap是空的,就把(pos,0)加入,如果非空,就把(pos,heap最高值)加入

# 为什么用到heap——因为要知道最大值
# 为什么用到hash,因为要删除特定值(height)的元素
# 所以hash要记录这个特定值(height)和在heap里的位置(index),以及记录重复:所以hash:{height:(index,count(个数))}

# 处理重复:如果同一高度的往里加,heap不变,hash里count+=1. delete方法反之
# 根据height,在hash里面找对应的index,然后在heap里删掉这个node,
# 删掉的方法是用跟leaf或root交换,然后调整,来完成.
# 注意hash_heap里没有pos这个变量
class HashHeap: #min_heap
    def __init__(self,mod):
        self.heap = []
        self.hash = {}  # item = (val,(index,count)) 此题里val是高度,index是在heap里的index,count(记录有几个有此高度的的点)
        self.size_t = 0
        self.mode = mod
    def peek(self):
        return self.heap[0]
    def size(self):
        return self.size_t
    def is_empty(self):
        return len(self.heap) == 0
    def parent(self,index):
        if index == 0:  #如果index=0,就没有parent
            return -1
        return (index - 1) / 2  #parent index
    def lson(self, index):
        return index * 2 + 1
    def rson(self, index):
        return index * 2 + 2
    def if_min(self,a,b):
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
        count_a = self.hash[val_a][1]   #这个值(val)在hash里对应的那个(index,count)里的count
        count_b = self.hash[val_b][1]
        self.hash[val_b] = (a, count_b)  #在hash里把index对换了
        self.hash[val_a] = (b, count_a)
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a] #在heap里把值对换了.
    def pop(self):
        self.size_t -= 1
        height = self.heap[0]  #root的值
        hash_now = self.hash[height]  #现在的hash的item
        if hash_now[1] == 1:     #如果这个height只出现过一次
            self.swap(0,(len(self.heap) - 1))  #把root跟最后一个leaf交换
            del self.hash[height]        #在hash里删掉root对应的item
            del self.heap[len(self.heap) - 1]  #在heap里删掉交换后的那个leaf
            if len(self.heap) > 0:
                self.shiftdown(0)
        else:          #如果这个height出现过多次,就把count-1
            self.hash[height] = (0,hash_now[1] - 1)
        return height
    def add(self, height):   #这里now是height
        self.size_t += 1
        if self.hash.has_key(height): #如果hash里面存过这个height,在hash里别的不变,count+=1,heap不变
            hash_now = self.hash[height]   #[index, count]
            self.hash[height] = (hash_now[0],hash_now[1] + 1)
        else:                     #如果hash里没存过这个height,hash加入这个,heap也加入这个在最后的位置上
            self.heap.append(height)
            self.hash[height] = (len(self.heap) - 1, 1)
        self.shiftup(len(self.heap) - 1) #在heap里把最后一个node向上调整

    def delete(self, height):  #now就是height
        self.size_t -= 1
        hash_now = self.hash[height] #[index, count]
        if hash_now[1] == 1:   #如果 这个height只出现过一次,
            self.swap(hash_now[0],len(self.heap)-1)  #把它跟最后那个位置交换,
            del self.hash[height]  # 在hash里删掉height对应的item
            del self.heap[len(self.heap) - 1]  # 在heap里删掉调换后的最后那个node
            if len(self.heap) > hash_now[0]:
                self.shiftup(hash_now[0])
                self.shiftdown(hash_now[0])
        else:
            self.hash[height] = (hash_now[0], hash_now[1] - 1)

    def shiftup(self, index): #此节点往上调整
        while self.parent(index) > -1:#如果有父节点
            parent_index = self.parent(index)
            if self.if_min(self.heap[parent_index], self.heap[index]):  #父节点上的value比此节点value小,就什么都不做
                break
            else:   #父比子小,就交换
                self.swap(parent_index,index)
            index = parent_index

    def shiftdown(self, index): #此节点往下调整
        while self.lson(index) < len(self.heap): #如果有左孩子
            left_index = self.lson(index)
            right_index = self.rson(index)
            if right_index >= len(self.heap) or self.if_min(self.heap[left_index], self.heap[right_index]):#如果没有右孩子或左孩子大于右孩子
                son = left_index #左孩子为那个要交换的node
            else:
                son = right_index #否则就是右孩子为要交换的node
            if self.if_min(self.heap[index], self.heap[son]): #如果此node比要交换的那个node小,就什么也不做
                break
            else:
                self.swap(index,son) #否则就交换
            index = son


class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers

    def comparator(self,x,y):
        if x[0] != y[0]:
            return x[0] - y[0]
        else:
            if x[2] and y[2]:  #如果都是左点
                return y[1] - x[1]   #谁高谁先
            elif not x[2] and not y[2]:
                return x[1] - y[1]    #谁高谁先
            else:
                if x[2]:
                    return x[2] - y[2]
                else:
                    return y[2] - x[2]
    def output(self, res):
        ans = []
        if len(res) > 0:
            pre = res[0][0]
            height = res[0][1]
            for i in range(1,len(res)):
                now = []
                index = res[i][0]
                if height > 0 and pre != index:   #(pre != index)为了避免同一个pos上两个点的重复划线
                    now.append(pre)
                    now.append(index)
                    now.append(height)
                    ans.append(now)
                pre = index
                height = res[i][1]
        return ans
    def buildingOutline(self, buildings):
        res = []
        if buildings is None or len(buildings) == 0 or len(buildings[0]) == 0:
            return res
        # edges = [pos, height, is_start] # True is left,False is right
        edges = []
        # 用[pos, height, is_start]的形式把所有点加入edges里.
        for building in buildings:
            # edges = [pos, height, is_start]
            # start
            edges.append([building[0], building[2], True])
            # end
            edges.append([building[1], building[2], False])
        # 排序 edges
        #如果pos不同,谁pos小谁先
        #如果pos相同,如果都是起点,谁高谁先,(因为高的盖住矮的)如果都是终点,谁矮谁先()
        # 如果一个是起点一个是终点,谁是起点,谁先
        # sorted(edges, key = lambda x:(x[0], x[1], x[2]))
        edges =sorted(edges, cmp = self.comparator)
        # 引入hash_heap
        hash_heap = HashHeap('max')
        # 往res里面加item, item = [pos,height]
        h = -1
        for edge in edges:#对于每一个点
            if edge[2]: #如果是左点
                # 如果hash_heap是空,或,点的height大于heap的root的值,把起(pos,height)加入res里
                # 说明新来的起点不会被覆盖,所以需要加进来
                if hash_heap.is_empty() or edge[1] > hash_heap.peek():
                    now = [edge[0], edge[1]]
                    if len(res)>0 and res[-1][0] == now[0] and h == now[1]: #处理的是一根线的right接着另一根先的left,这时要把right点去掉,并且left点也不能记入.
                        del res[-1]                                         #判断是否是重合点,1看pos一致不,2看高度一致不,这个高度是上一点的高度h,而不是res里最后一个元素的高度res[-1][1]
                    else:
                        res.append(now)
                hash_heap.add(edge[1])  #在hash_heap里加入这个node的height
            else: #如果是右点
                h = edge[1]
                hash_heap.delete(h)  #在hash_heap里删掉这个node的height
                # 如果hash_heap是空,或,点的height大于heap的root的值,
                if hash_heap.is_empty() or edge[1] > hash_heap.peek():
                    #如果hash_heap是空,把起(pos,0)加入res里
                    if hash_heap.is_empty():
                        now = [edge[0], 0]
                    else: #否则把起(pos,root的值)加入res里
                        now = [edge[0], hash_heap.peek()]
                        #不能(now = [edge[0],edge[1]]).因为这里记入的是这个点的pos和当前的heap最高点,而不是这个点的height,因为这个点如果是右点就不能记入他的高度
                    res.append(now)

        x = self.output(res)
        return x
if __name__ == '__main__':
    s = Solution()

    a = [[3,7,78],[4,5,313],[5,8,401],[6,10,242],[7,8,600],[8,12,466]]
    # yes =[[3,4,78],[4,5,313],[5,7,401],[7,8,600],[8,12,466]]
    # no [[3, 4, 78], [4, 5, 313], [5, 5, 313], [5, 7, 401], [7, 8, 600], [8, 8, 600], [8, 12, 466]]
    # no [[3, 4, 78], [4, 5, 313], [5, 5, 78], [5, 7, 401], [7, 8, 600], [8, 8, 242], [8, 12, 466]]

    #a = [[1,10,3],[2,5,8],[7,9,8]]
    # yes [[1, 2, 3], [2, 5, 8], [5, 7, 3], [7, 9, 8], [9, 10, 3]]
    #a = [[827,830,397],[828,832,681],[829,832,180],[830,834,414],[831,834,410],[832,837,681],[833,836,748],[834,838,403]]

    print s.buildingOutline(a)


    #yes [[827,828,397],[828,833,681],[833,836,748],[836,837,681],[837,838,403]]
    #no [[827, 828, 397], [828, 832, 681], [832, 833, 681], [833, 836, 748], [836, 837, 748], [837, 838, 681]]