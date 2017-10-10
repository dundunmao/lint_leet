# -*- encoding: utf-8 -*-
class Solution(object):
    def __init__(self):
        self.pointer= 0
        self.count= 0
        self.buff = ['']*4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        ptr = 0
        while ptr < n:
            if self.pointer == 0:
                self.count = read4(self.buff)
            if self.count == 0:
                break
            while ptr < n and self.pointer < self.count:
                buf[ptr] = self.buff[self.pointer]
                ptr += 1
                self.pointer += 1
            if self.pointer >= self.count:
                self.pointer = 0
        return ptr
# Just keep copying as long as more is both desired and available (read more on the fly when needed).
class Solution1(object):
    def __init__(self):
        self.i4= 0
        self.n4= 0
        self.buff4 = ['']*4
    def read(self, buf, n):  #buf开始是空的，要从内存里读n个到buf里，self.buff是每次用read4读进来的四个（或少于4个）数
        # // internal buffer: i4, n4, buf4
        # // external buffer: i, n, buf
        i= 0
        while i < n :
            if self.i4 >= self.n4:  #i4是在buff4里的指针，用力啊遍历buff4，挨个铐进buf里的，每次i4超过n4就归置为0
                self.n4 = read4(self.buff4)   #表示再继续读进来几个数，同时用了API也就存在self.buff4里了
                self.i4 = 0                  #i4从头开始等到遍历
                if self.n4 == 0:   #读完了，读不进来了
                    break
            buf[i] = self.buff4[self.i4]
            i += 1
            self.i4 += 1
        return i

def read4(buf):
    return
