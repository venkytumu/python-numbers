#write a program to find the smallest of the three numbers
a=int(input("enter a frist number:", ))
b=int(input("enter a second number:", ))
c=int(input("enter a thrid number:",  ))
if (a<b and a<c):
    print("a is smaller than b and c")
elif (b<a and b<c):
    print("b is smaller than a and c")
else:
    print("c is smaller than a and b")
