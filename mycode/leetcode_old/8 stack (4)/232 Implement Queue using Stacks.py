# -*- encoding: utf-8 -*-
# 标签：Stack
# 题目；用stack表示queue
# 思路：把一个stack POP出去塞入另一个stack（就是1，2，3，4，要取1但是必须从尾巴出来，就得从尾巴把别的数都pop出来）
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x):
        self.stack1.append(x)
    def pop(self):
        if len(self.stack2)!=0:
            self.stack2.pop()
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())                 #把stack1里的数边POP边往stack2里压
            self.stack2.pop()
    def peek(self):                   #第一个数
        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
    def empty(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        else:
            return False