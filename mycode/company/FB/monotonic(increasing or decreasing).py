def monotonic(a):
    i = 1
    if a[i-1] < a[-1]:
        while i<len(a):
            if a[i-1] > a[i]:
                return False
            i += 1
    elif a[i-1] > a[-1]:
        while i<len(a):
            if a[i-1] < a[i]:
                return False
            i += 1
    else:
        while i<len(a):
            if a[i-1] != a[i]:
                return False
            i += 1
    return True
if __name__ == '__main__':
    a = [1, 1, 2, 2, 3]
    print monotonic(a)
    a = [1, 2, 3, 2, 1]
    print monotonic(a)
    a = [1, 1, 1]
    print monotonic(a)
