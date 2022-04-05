#bitwise operators
#AND Bitwise operator(&)
#returns 1 if both bits are 1
'''
a=10-------1010
             &
b=4--------0100
        ------------
           0000
        ------------
'''

#2----0010
#3----0011
#  -------
#     0010
#  --------
#OR Bitwisenoperator(|)
#returns 1 if either of the bit is 1 else 0
#2----0010
#3----0011
#    --------
# |   0011
#    -------
#NOT operator
#returns one's complement of the number
# a=2----0010
  #     +   1
#   __________
#        0011
#   ----------
#XOR Bitwise Operator(^)
#Returns 1 if one of the bits is 1 and other is 0 else returns Flase
#2-----0010
#3-----0011
# ^   ---------
#      0001
#     ----------
n=int(input())
m=int(input())
while m!=0:
    c=n&m #AND operstor
    n=n^m #XOR Bitwise operator
    m=c<<1 #shift left operator
print('sum of two number:',n)

mmm




































