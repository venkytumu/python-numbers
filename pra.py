n=int(input())

sum=0
while n>0:
    p=n**2
    k=p%10
    sum=sum+k
    n=p//10
if sum==n:
    print("neon")
else:
    print("not neon")
