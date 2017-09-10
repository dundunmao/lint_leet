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
