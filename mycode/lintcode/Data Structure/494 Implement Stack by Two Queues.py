# coding:utf-8
# 利用两个队列来实现一个栈的功能
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# push(1)
# pop()
# push(2)
# isEmpty() // return false
# top() // return 2
# pop()
# isEmpty() // return true
from Queue import Queue
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.q1.put(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())
        self.q1.get()
        self.q1 = self.q2

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        for i in range(self.q1.qsize()-1):
            self.q2.put(self.q1.get())
        t = self.q1.get()
        self.q2.put(t)
        self.q1 = self.q2
        return t

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return self.q1.empty()
if __name__ == '__main__':


    s = Stack()
    print s.push(1)
    print s.push(2)
    print s.pop()
    print s.top()

    print s.isEmpty()
    print s.push(2)
    print s.isEmpty()
    print s.top()
    print s.pop()
    print s.isEmpty()