# -*- encoding: utf-8 -*-


# from collections import  defaultdict
# hash = defaultdict(int) #list指value的类型
# x = [1,1,3,4]
# for ele in x:
#     hash[ele]=0

# from collections import  Counter
# x = [1,1,3,4]
# c = Counter(x)
# print c[1]

x = [1,1,3,4]

new = {4:10}
dic = {1: 0, 3: 0, 4: 10}
for key in x:
    new.setdefault(key,0)
    print key, x


new = {4:10}
dic = {1: 0, 3: 0, 4: 10}
for key in x:
    x = new.setdefault(key,0)
    print key, x


new = {}
dic = {1: [0, 0], 3: [0], 4: [0]}
for (key, value) in dic.items():
    new.setdefault(key, []).append(value)



new = {}
dic = {1: [0, 0], 3: [0], 4: [0]}
for (key, value) in dic.items():
    group = new.setdefault(key, []) # key might exist already
    group.append( value )



for ele in x:
    dic.setdefault(ele,0)
print dic


class A():
    def __init__(self):
        self.abc = 0
    def helper(self,a):
        b = []
        b.append(a)
        return b

a = A()
for i in range(10):
    a.helper('1')
    print a
print a

if __name__ == "__main__":
    num = 10
