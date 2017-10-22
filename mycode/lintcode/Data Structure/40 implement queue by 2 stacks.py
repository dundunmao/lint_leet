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
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            return None
        stack2 = []
        for i in range(len(self.stack1)):
            stack2.append(self.stack1.pop())
        ans = stack2.pop()
        while stack2:  # 注意这里是x的长度
            self.stack1.append(stack2.pop())
        return ans

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            return None
        stack2 = []
        while self.stack1:
            stack2.append(self.stack1.pop())
        ans = stack2[-1]
        while stack2:  # 注意这里是x的长度
            self.stack1.append(stack2.pop())
        return ans

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0
# 求min-queue
class MyQueue0(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.min_stack1 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack1) > 1:
            self.min_stack1.append(min(x,self.min_stack1[-1]))
        else:
            self.min_stack1.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            return None
        stack2 = []
        min_stack2 = []
        for i in range(len(self.stack1)):
            x = self.stack1.pop()
            self.min_stack1.pop()
            stack2.append(x)
            if len(min_stack2) > 1:
                min_stack2.append(min(x, min_stack2[-1]))
            else:
                min_stack2.append(x)
        ans = stack2.pop()
        min_stack2.pop()
        while stack2:  # 注意这里是x的长度
            cur = stack2.pop()
            self.stack1.append(cur)
            if len(self.stack1) > 1:
                self.min_stack1.append(min(cur, self.min_stack1[-1]))
            else:
                self.min_stack1.append(cur)
        return ans
    def min_queue(self):
        return self.min_stack1[-1]
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            return None
        stack2 = []
        while self.stack1:
            stack2.append(self.stack1.pop())
        ans = stack2[-1]
        while stack2:  # 注意这里是x的长度
            self.stack1.append(stack2.pop())
        return ans

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
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
    print s.min_queue()
    print s.pop()
    print s.pop()
    print s.min_queue()