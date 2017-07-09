class FooParent(object):
    def __init__(self):
        self.parent = 'I am the parent'
        print'Parent'
    def bar(self, message):
        print message, 'from Parent'
class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print'Child'
    def bar(self, message):
        FooParent.bar(self, message)
        print 'Child bar function'
        print self.parent
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar("hello world")


class FooParent(object):
    # def __init__(self):
    #     self.parent = 'I am the parent'
    #     print'Parent'
    def bar(self, message):
        print message, 'from Parent'
class FooChild(FooParent):
    def __init__(self):
        # FooParent.__init__(self)  #如果FootParent改了,这里也要改
        super(FooChild,self).__init__() #但是如果用super,这里就不用改.
        print'Child'
    def bar(self, message):
        # FooParent.bar(self, message)
        super(FooChild,self).bar(message)
        print 'Child bar function'
        print self.parent
if __name__ == '__main__':
    a = FooParent()
    a.bar("yes")
    fooChild = FooChild()
    fooChild.bar("hello world")