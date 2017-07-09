
class PhoneLog():
    """
    Records a phone log like what you see in your phone.
    """
    def __init__(self):
        self.store = []
        self.log = None
    def record_incoming_call(self, caller, duration):
        """
        Record an incoming call from caller to the User.
        """
        # print "some call information "
        # store = []
        # store = []
        self.store.append([caller,duration,"incoming"])
        # return incoming_call

    def show_incoming_calls(self):
        """
        Return a list of all incoming call information.
        """
        # if hasattr(self, 'store'):
        #     return self.store
        incoming_list = []
        for item in self.store:
            if item[2] == "incoming":
                incoming_list.append(item[0]+', '+str(item[1]))
        return '; '.join(incoming_list)

    def record_outgoing_call(self, callee, duration):
        """
        Record an outgoing call from the User to a callee.
        """
        self.store.append([callee, duration, "outgoing"])
        pass

    def get_longest_called(self):
        """
        Return the name or names of the individuals who were on the longest
        single call with the User.
        """
        sort_store = sorted(self.store, key = lambda x:x[1])
        return sort_store[-1][0]

    def log(self):
        file = open('log.txt','w')
        for line in self.store[-1]:
            file.write(line+'\n')
        file.close()


if __name__ == "__main__":
    call_log = PhoneLog()
    call_log.record_incoming_call("Jack", 1)
    call_log.record_incoming_call("Mike", 7)
    call_log.record_outgoing_call("Jil", 14)
    # store = call_log.record_incoming_call("Mike", 7)
    print call_log.get_longest_called()

    print call_log.show_incoming_calls() # should return jack, 1; jil, 14;

    assert call_log.get_longest_called() ==  "Jil" , "Jil should be longest called"