#subtract of two number without using minus(-)operator
num1=int(input("enter a number1:", ))
num2=int(input("enter a number2:", ))
sub=num1+(~num2+1)#num2 is 2's compliment of the number
print("subtraction of two numners:", sub)
