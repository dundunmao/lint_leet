# coding:utf-8
class PhoneLog():
    """
    Records a phone log like what you see in your phone.
    """
    empCount = 0
    # store = []
    # def __init__(self):
    #     self.store = []
    #     self.log = None
    def record_incoming_call(self, caller, duration):
        """
        Record an incoming call from caller to the User.
        """
        # print "some call information "
        # self.store = []
        self.store.append([caller,duration])
        # return incoming_call

    def show_incoming_calls(self):
        """
        Return a list of all incoming call information.
        """
        # if hasattr(self, 'store'):
        #     return self.store
        return self.store

    def record_outgoing_call(self, callee, duration):
        """
        Record an outgoing call from the User to a callee.
        """
        print "Total Employee %d" % PhoneLog.empCount
        self.store = [] #instance public varable, 当这个函数调用过后,这个x就存在了,其他函数就可以调用它了.
        self.y = 1

    def get_longest_called(self):
        """
        Return the name or names of the individuals who were on the longest
        single call with the User.
        """
        print self.empCount

        return self.y
        # return { "Jil" }

    def log(self):
        pass

if __name__ == "__main__":
    call_log = PhoneLog()
    # PhoneLog.store = []   #动态添加class variable
    call_log.record_outgoing_call("Jil", 14)
    call_log.record_incoming_call("Jack", 1)
    call_log.record_incoming_call("Mike", 7)


    # store = call_log.record_incoming_call("Mike", 7)
    # new_store = []
    # for i in so
    print call_log.get_longest_called()


    print call_log.show_incoming_calls() # should return jack, 1; jil, 14;
