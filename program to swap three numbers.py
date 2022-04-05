#program to swap three numbers
num1=int(input('enter a number1:', )) #10
num2=int(input('enter a number2:', )) #15
num3=int(input('enter a number3:', )) #20
num1=num1+num2+num3 #10+15+20=45
num2=num1-num2-num3 #45-15-20=10
num3=num1-num2-num3 #45-10-20=15
num1=num1-num2-num3 #45-10-15=20
print('number1:',num1)
print('number2:',num2)
print('number3:',num3)
