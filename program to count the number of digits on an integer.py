#program to count the number of digits on an integer
n=int(input("enter a number:", ))#12345
count=0 #1,2,3,4,5
while n>0:#12345,1234,123,12,1,0(false)
    n=n//10 #12345//10=1234,1234//10=123,123//10=12,12//10=1,1//10=0
    count+=1 #0+1=1,1+1=2,2+1=3,3+1=4,4+1
print(count)
