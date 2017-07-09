__author__ = 'eva'

class LinkedList(object):

    class Element(object):

        def __init__(self,list,datum,next):
            self.__list = list
            self.__datum = datum
            self.__next = next

        def getDatum(self):
            return self.__datum

        datum = property(
            fget = lambda self: self.getDatum())

        def getNext(self):
            return self.__next

        next = property(
            fget = lambda self: self.getNext())

    def __init__(self):

        self.__head = None
        self.__tail = None

    def getHead(self):
        return self.__head
    head = property(
        fget = lambda self: self.getHead())
    def prepend(self,item):
        tmp = self.Element (self,item,self.__head)
        if self.__head is None:
            self.__tail = tmp
            self.__head = tmp

    def insert(self, pos, item):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
          p = p.__next
          i += 1
        if p == None or i > pos-1:
          return -1
        tmp = self.Element(self, item, p.__next)
        p.__next = tmp
        return 1
    def getItem(self, pos):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
          p = p.__next
          i += 1
        if p == None or i > post-1:
          return -1
        return p.__datum
    def delete(self, pos):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
          p = p.__next
          i += 1
        if p == None or i > post-1:
          return -1
        q = p._next
        p.__nex = q.__next
        datum = p.__datum
        return datum
    def setItem(self, pos, item):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
          p = p.__next
          i += 1
        if p == None or i > post-1:
          return -1
        p.__datum = item
        return 1
    def find(self, pos, item):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
            if p.__datum == item:
                return 1
            p = p.__next
            i += 1
        return -1
    def empty(self):
        if self.__head == None:
            return 1
        return 0
    def size(self):
        i = 0
        p = self.__head
        while p != None and i < pos -1:
            p = p.__next
            i += 1
        return i

    def clear(self):
        self.__head = None
        self.__tail = None

if __name__ == "__main__":
    test = LinkedList()
    test.prepend('test0')
    print test.insert(1, 'test')
    print test.head.datum
    print test.head.next.datum