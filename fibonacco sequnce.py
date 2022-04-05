#fibonacco sequnce
   ''' 0 1 1 2 3 5 8 13 21 34
       '''


 n=int(input())
a=0
b=1
print(a,b,end=" ")
while(a+b<=n):
    c=a+b
    print(c,end="  ")
    a=b
    b=c
    
