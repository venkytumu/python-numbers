num1=int(input())
num2=int(input())
div=0 #1,2,3,4,5,6
while num1>=num2:#12>2=true,10>2=true,8>2=true,6>2=true,4>2=true,2>=2,0>=2=false
    num1=num1-num2 #num1=12-2=10,10-2=8,8-2=6,6-2=4,4-2=2,2-2=0
    div+=1 #0+1=1,1+1=2,2+1=3,3+1=4,4+1=5,5+1=6
print("Division of two number:", div)
