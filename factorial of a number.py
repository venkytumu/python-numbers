#write a program to find the factorial of a number
#3=3*2*1
n=int(input("enter a number:", ))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(i,fact)
print("factorial of a number:",fact)
