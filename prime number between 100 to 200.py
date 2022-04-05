n=int(input())
for num in range(100,n):
  if all(num%i!=0 for i in range(2,num)):
    print(num)
