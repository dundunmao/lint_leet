def stringComparator(s,t):
    ls = len(s)
    lt = len(t)
    le = min(ls,lt)
    i = 0
    j = 0
    while i < le:
        if s[i].isalpha():
            if t[j].isalpha():
                if s[i]>t[j]:
                    return s
                elif s[i]< t[j]:
                    return t
            elif t[j].isdigit():
                return s
        elif s[i].isdigit():
            if t[j].isalpha():
                return t
            if t[j].isdigit():
                container_s = []
                container_t = []
                while s[i].isdigit():
                    container_s.append(s[i])
                    i+=1
                while t[i].isdigit():
                    container_s.append(t[j])
                    j+=1
                if int(''.join(container_s)) > int(''.join(container_t)):
                    return s
                elif int(''.join(container_s)) < int(''.join(container_t)):
                    return t
        i += 1
        j += 1
        if s[i]:
            return s
        elif t[j]:
            return t
if __name__ == '__main__':
    s = 'abc123aca'
    t = 'abc123acd'
    print stringComparator(s, t)