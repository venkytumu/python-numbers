s=input()
l=len(s)
for  i in range(-1,(-l-1),-1):
    print(s[i],end='')
    print()
print(s[-1::-1])
