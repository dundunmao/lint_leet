#combination
# anagram
def comb(a,b):
    if len(a)!=len(b):
        return False
    return set(a)==set(b)