
class Dequeue(object):

    def __init__(self):
        # do some intialize if necessary
        self.head = None
        self.tail = None

    # @param {int} item an integer
    # @return nothing
    def push_front(self, item):
        # Write yout code here
        node = ListNode(item)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = self.head
    # @param {int} item an integer
    # @return nothing
    def push_back(self, item):
        # Write yout code here
        node = ListNode(item)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
    # @return an integer
    def pop_front(self):
        # Write your code here
        if self.head:
            node = self.head
            self.head = self.head.next
            node.next = None
            if self.head is None:
                self.tail = self.head
        else:
            return None
        return node.val
    # @return an integer
    def pop_back(self):
        # Write your code here
        if not self.tail:
            return None
        elif self.tail == self.head:
            node = self.tail
            self.tail = None
            self.head = None
            return node.val
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            node = self.tail
            cur.next = None
            self.tail = cur
            return node.val
            