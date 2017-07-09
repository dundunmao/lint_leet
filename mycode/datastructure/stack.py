__author__ = 'eva'

import exceptions

# class method and instance method can call class variable
# only instance method can call instance variable
# class method is called as format: class_name.method
# instance method is called as format: self.method
# instance method can call class method, but vice versa not true

class Stack():
    __implementation_type = "Implemntation of Stack data structure using Python list" #class variable, private, lowest
    __max_size = 1000000
    @staticmethod #class method
    def print_implementation_way():
        print Stack.__implementation_type
        return

    def __init__(self, size):
        self.__size = size

        if size > Stack.__max_size:
            resize_value = Stack.__max_size
            print "do not use size larger than " + str(Stack.__max_size)
            self.__size = resize_value #resize_value will not exist after this line
        self.__items = []
        self.__top = -1    #????????

    def push(self, ele):
        if self.isfull():
            raise Exception("out of range")
        else:
            self.__items.append(ele)
        self.__top=self.__top + 1


    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            self.__top = self.__top - 1
        return self.__items.pop()




    def get_top(self):
        if self.is_empty():
            return None
        return self.__items[self.__top]

    def isfull(self):
        return self.__top + 1 == self.__size

    def is_empty(self):
        return self.__top == -1
    def print_stack(self):
        print self.__items

    def get_size(self):
        return len(self.__items)

if __name__ == "__main__":
    s = Stack(20)
    print s.get_size()
    for i in range(3):
        s.push(i)
        #print s.pop()

    s.print_stack()