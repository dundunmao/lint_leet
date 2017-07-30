# coding:utf-8
# 实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。
#
# 你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。
#
#  注意事项
#
# 如果堆栈中没有数字则不能进行min方法的调用
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1
class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_stack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        self.min_stack.append(min(self.stack))

    def pop(self):
        # pop and return the top item in stack

        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None
if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    print s.pop()
    s.push(2)
    s.push(3)
    print s.min()
    s.push(1)
    print s.min()