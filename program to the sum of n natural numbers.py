#write a program to the sum of n natural numbers
n=int(input('enter a number :', ))
#sum=n*(n+1)/2
#print('sum of n natural numbers:',sum)
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of n natural numbers:",sum)
