#python using split method
#taking two inputs at a time
#syntax using split() method
#input().split(separator, maxsplit)
x,y=input("enter a two value:").split()
print(x)
print(y)
#Using List Comprehension
x,y=[int(x) for x in input("enter two value:").split()]
print(x)
print(y)
