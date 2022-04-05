l=[10,11,12,13,14,15,16,17,19,20]
'''
sum=0
prd=1
i=0
while (i<len(l)):
    a=(l[i])
    i=i+1
    sum=sum+a
    prd=prd*a
print(sum)
print(prd)

for i in l:
    sum+=i
print(sum)

#reverse
l.reverse()
print(l)
'''
#reverse by using loop
print(len(l))
i=0
while i<=len(l):
    a=l.pop()
    print(a)
    i+=1
print(a)
