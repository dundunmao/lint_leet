

def compareStrings(string):
    result = []
    i = 0
    while i<len(string):
        count = 1
        while i+1 < len(string) and string[i] == string[i+1]:
            count+=1
            i+=1
        pair = [string[i],count]
        result.extend(pair)
        i+=1
    print result
    return ''.join(str(i) for i in result)


if __name__ == "__main__":
    s = "aaabbcddddeeea"
    print compareStrings(s)