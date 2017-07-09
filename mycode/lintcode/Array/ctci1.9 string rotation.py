
def isSbustring(string):
    pass

def rostr(string):
    i = len(string)-1
    while i>0:
        string = string[1:]+string[0]
        if isSbustring(string):
            return False
        i -= 1
    return True

