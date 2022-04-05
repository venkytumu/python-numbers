#write program to check a year is a leap year or  not
n=int(input())
if ((n%100!=0 or n%400) and (n%4==0)):
    print('leap year')
else:
    print("not a leap year")
