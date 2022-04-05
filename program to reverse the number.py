#write a program to reverse a number
n=int(input("enter a number:", ))#12345
a=0 #5,54,
while (n!=0):#12345,1234
    b=n%10 # 12345%10=5,1234%10=4
    n=n//10 #12345//10=1234,1234//10=4
    a=a*10+b # 0*10+5=5,5*10+4=54
    
print(a)
    
