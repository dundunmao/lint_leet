# coding:utf-8


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.s = []
    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.s.append(x)
    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        item = self.s[-1]
        self.s = self.s[:-1]
    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        return self.s[-1]
    # @return a boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        if len(self.s) == 0:
            return True
        else:
            return False