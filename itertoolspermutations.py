'''
Sample Input
HACK 2
Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

from itertools import permutations

mystr,n=input().split()
n=int(n)

reslist=sorted(list(permutations(mystr,n)))

res=[]
for i in reslist:
    print("".join(i))


    