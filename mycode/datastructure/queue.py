__author__ = 'eva'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.__items = [] # "__" means private
        self.__nn = "sfdsf"

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop(0)

    def is_empty(self):
        return self.get_size() == 0


    def get_size(self):
        return len(self.__items)

    def print_queue(self):
        print self.__items

    def get_nn(self):
        return self.__nn

if __name__ == "__main__":

    q = Queue()
    for i in range(10):
        q.push(i)
    q.print_queue()

    print q.is_empty()

    for i in range(0,q.get_size()):
        q.pop()
    q.print_queue()
    # q.__nn = "7786"

    #print q.__nn
    print q.get_nn()