#Divsion two number without using division function(/)
num1=int(input("enter a number1:", ))
num2=int(input("enter a number2:", ))
div=0
while num1>num2:
    num1=num1-num2
    div+=1
print('division of two numbers:',div )
