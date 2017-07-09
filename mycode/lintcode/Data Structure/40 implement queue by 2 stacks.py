# coding:utf-8
# 正如标题所述，你需要使用两个栈来实现队列的一些操作。
#
# 队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。
#
# pop和top方法都应该返回第一个元素的值。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        return self.stack1[0]
    def pop(self):
        # write your code here
        # pop and return the top element
        for i in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        p = self.stack1.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return p
if __name__ == '__main__':

    s = MyQueue()
    # print s.push(1)
    # print s.pop()
    # print s.push(2)
    # print s.push(3)
    # print s.top()
    # print s.pop()

    print s.push(1)
    print s.push(2)
    print s.push(3)
    print s.push(4)
    print s.push(5)
    print s.pop()
    print s.pop()
    print s.push(6)
    print s.push(7)
    print s.push(8)
    print s.push(9)
    print s.pop()
    print s.pop()