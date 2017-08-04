# coding:utf-8
# 为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。
#
# 获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。
#
# 写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置。

# 单向链表,指向prev.
class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
class LRUCache1:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    # append到队尾
    def push_back(self, node):
        #加入hash
        self.hash[node.key] = self.tail
        #加入linked list
        self.tail.next = node
        self.tail = node

    # pop排头
    def pop_front(self):
        # 在hash里删掉head后面那个node
        del self.hash[self.head.next.key]
        # 在linked list里,删掉head后面那个node
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    # 删掉node,加到队尾.
    def kick(self, prev):  #注意这里是prev
        # 删掉那个点
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next   #删linked list里的node,就是prev的下一个点
        if node.next is not None:
            self.hash[node.next.key] = prev  #删hash里的node
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])  #kick掉的是key的下一个node
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


#################################################################
# 双向链表的方法.
# 本来是用dictionary存(key,value)的
# 然后存的时候同时还存了一遍双向列表,每个node里还有key的信息.
# 用链表是为了:删旧node时只要删head处,添加新node时加在tail处.
# 用双向的,因为删存在的node时,好找.
class dNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key  #在linked list里的index
        self.pre = None
        self.next = None

class LRUCache2:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.curSize = 0
        self.hash = {}  # 存dqlist里的key和node的关系
        self.head = dNode(-1, -1)
        self.tail = dNode(-1, -1)
        self.head.next = self.tail #这里的head,tail都是dummy node
        self.tail.pre = self.head

    # 如果有这个node,step1:从原来的位置把它删掉,step2:tail上填上这个node.
    def moveToTail(self, pnode):
        # 把它从原来的位置删除
        if pnode.pre:
            pnode.pre.next = pnode.next
        if pnode.next:
            pnode.next.pre = pnode.pre
        # 添加到tail前面
        self.tail.pre.next = pnode
        pnode.pre = self.tail.pre
        pnode.next = self.tail
        self.tail.pre = pnode
        #这里在hash里key对应的node是不变的,所以没有操作hash
    # 从head处删掉一个node
    def remove_head(self):
        pdel = self.head.next
        self.head.next = pdel.next
        pdel.next.pre = pdel.pre
        del self.hash[pdel.key]

    def add(self, key, value):
        newNode = dNode(key, value)
        # add to dict
        self.hash[key] = newNode
        # add to tail of dqueue
        self.moveToTail(newNode)
    # @return an integer
    def get(self, key):  #给以个index(就是key),得到一个value.就是index对应的那个数
        if self.hash.has_key(key):
            pvalue = self.hash[key] #这是个node
            value = pvalue.val #求出node的值,返回的就是它
            # get操作就是访问它了,所以要把他放在linked list的尾巴,
            self.moveToTail(pvalue)
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):  #在key那个位置插入value.
        # 如果已经有这个key了,就更新这个key
        if self.hash.has_key(key):
            self.hash[key].val = value
            self.moveToTail(self.hash[key])
        # 如果没有就要插入这个key
        # 1) curSize < capacity, just add
        # 2) curSize == capacity, remove LRU and add
        else:
            self.add(key, value)
            if self.curSize < self.capacity:
                self.curSize += 1
            else:
                self.remove_head()
#######################################################
# 直接用dictionary,加time stamp.这种方法会超时.
from datetime import datetime
class LRUCache3:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dict = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if self.dict.has_key(key):
            v = self.dict[key][0]
            t = datetime.now()
            self.dict[key] = [v,t]
            return v
        else:
            return -1

    def set(self, key, value):

        #如果有足够地方
        if len(self.dict) < self.capacity:
            t = datetime.now()
            self.dict[key] = [value,t]
        #如果已经满了
        else:
            #如果key在里面,就更新它
            if self.dict.has_key(key):
                t = datetime.now()
                self.dict[key] = [value,t]
            #如果key不在里面,就删除最早的,再加入它
            else:
                # 找到最小时间的key,删掉这个item
                sorted_array = sorted(self.dict.items(), key=lambda d: d[1][1])
                del self.dict[sorted_array[0][0]]
                t = datetime.now()
                self.dict[key] = [value,t]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache_leet(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        head_next.prev = node
        node.next = head_next

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            self.remove(self.d[key])
        node = Node(key, value)
        self.add(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            tail_prev = self.tail.prev
            self.remove(tail_prev)
            del self.d[tail_prev.key]


if __name__ == '__main__':

    s = LRUCache_leet(2)
    s.put(2,1)
    s.put(1,1)
    s.get(2)
    s.put(4,1)
    s.get(1)
    s.get(2)
    # print s.hash
