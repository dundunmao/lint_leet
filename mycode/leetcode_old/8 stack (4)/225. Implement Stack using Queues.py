# -*- encoding: utf-8 -*-
# 标签：Stack
# 题目；用queues表达stack
# 思路：用collections.deque()里的popleft方法pop出list[0]，把队头拿出来放队尾，一直到队头为原来的最后一个数，把这时候的队头pop出来(比如1，2，3，4，我要取4，只有前头有开口，就取1然后放队尾，再取2放队尾，再取3放队尾，最后4就从头部出来了)




import collections

class Stack(object):
    def __init__(self):
        self.stack = collections.deque([])
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())   #边把队头拿出来边放队尾，一直到队头为原来的最后一个数（4，1，2，3）
        self.stack.popleft()   #把这时候的队头pop出来
    def top(self):
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0

if __name__ =="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
