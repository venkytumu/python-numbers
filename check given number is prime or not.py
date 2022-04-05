#program to check the given number is a prine or not
n=int(input("enter a number:", ))
factor_count=0
for i in range(1,n+1):
    if(n%i==0):
        factor_count+=1
if (factor_count==2):
    print("prime")
else:
    print("not a prime")
