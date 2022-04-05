'''
def I(n):
    s = '+'
    for i in range(n):
        s += s
        return s

for x in I(2):
    print(x,end='')'''
'''
def fun(inp=2,out=3):
        return inp * out
print(fun(out=2))
'''
'''
class A:
 def __init__(self,v = 1):
    self.v = v
 def set(self,v):
        self.v = v
        return v
a =A()
print(a.set(a.v + 1))
'''
'''
class A:
     X = 0
     def __init__(self,v = 0):
                self.Y = v
                A.X += v
a = A()
b = A(1)
c = A(2)
print(c.X)
'''
class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()
