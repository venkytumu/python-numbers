#write a program to check wheather a given character is an Upper case,Lower case,Number or Special Character
n=input("enter a character:" )
if (n>='a' and n<='z'):
    print("The character is lower case")
elif(n>='A' and n<='Z'):
    print("the character is upper case")
elif (n>='0' and n<='9'):
    print("the  character is number")
else:
    print("the character is special character")
