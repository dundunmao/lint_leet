__author__ = 'eva'

class Node:
    def __init__(self,val=None,p=None):
        self.data = val
        self.next = p

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def buildList(self, array):
        # self.head = None
        # self.tail = None
        for i in array:
            new_node = Node(i, None)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        return self.head
    def printList(self):
        tempNode = self.head
        while(tempNode != None):
            print tempNode.data,
            tempNode = tempNode.next
        print ('')
    def getlength(self):
        p =  self.head
        length = 0
        while p != None :
            length+=1
            p = p.next
        return length

    def append(self,data):
        q = Node(data,None)
        if self.head == None:
            self.head = q
        else:
            p = self.tail
            p.next = q
        return self.head
    def delete_end(self):
        if self.head == None:
            print 'Linklist is empty.'
            return

        p = Node(self.getitem(0),None)
        #q = Node(self.getitem(0),None)
        i = 1
        for i in range(self.getlength()-1):
            #p = Node(self.getitem(i),None)
            post = p
            p.next = Node(self.getitem(i),None)

            q = Node(self.getitem(i),None)
            i += 1
        self.head = post
        self.tail = q
        return

    def getitem(self,index):
        if self.head == None:
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head
        while p.next!=0 and j <index:
           p = p.next
           j+=1
        if j ==index:
           return p.data
        else:
             print 'target is not exist!'
    def insert(self,index,item):
        if self.is_empty() or index<0 or index >self.getlength():
           print 'Linklist is empty.'
           return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
           q = Node(item,p)
           post.next = q
           q.next = p

    def delete(self,index):
        if self.head == None:
            print 'Linklist is empty.'
            return
        if index ==0:
            q = Node(item, self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            post.next = p.next



if __name__ == "__main__":
    myArray = [1,2,3,4]

    myList = LinkedList()
    myList.buildList(myArray)

    myList.printList()
    # print myList.getitem(2)
    # print myList.getlength()
    myList.delete_end()
    myList.printList()
    myList.append(11)
    myList.printList()