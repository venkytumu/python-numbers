#program to the sum of the  of all digits of a number
n=int(input('enter a number:', ))
while n>0:
    rem=n%10
    sum=sum+rem
    n=int(n/10)
print('the sum of digits of number is:', sum)
