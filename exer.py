x=int(input())
y=int(input())
while(x!=0):
    x=x/10
    x=x*y+x
    x=x%10
    y=y+1
print(x+y)
