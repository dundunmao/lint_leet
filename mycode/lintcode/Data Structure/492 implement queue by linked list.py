# coding:utf-8


class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None
class MyQueue(object):
    def __init__(self):
        # do some intialize if necessary
        self.head = None
        self.tail = None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        node = ListNode(item)
        node.next = None
        if not self.tail:
            self.head = node
            self.tail = self.head  # ,tail = head这个别忘了
        else:
            self.tail.next = node
            self.tail = node
            # self.tail = self.tail.next
    # @return an integer
    def dequeue(self):
        # Write your code here
        if not self.head:
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        if not self.head:
            self.tail = self.head      #当head是空时,tail = head这个别忘了

        return node.val



if __name__ == '__main__':

    q = MyQueue()

    q.enqueue(1)
    print q.dequeue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    q.enqueue(4)
    # q.enqueue(324)
    print q.dequeue()
