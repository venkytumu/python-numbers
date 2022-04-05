#print the even digit count and odd digit count of the given number
#n=1234
#2 odd digit 2 even digit ,0 is even
n=int(input())
even_count=0
odd_count=0
zero_count=0
t=n
while(n):
    r=n%10
    if (r==0):
        zero_count+=1
    elif(r%2==0):
        even_count +=1
    else:
        odd_count +=1
    n=n//10
print('there are',even_count,"even number and",odd_count,"odd number and",zero_count,"zeroes in a given n is",t) 
