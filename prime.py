#Check Prime
from math import sqrt

flag=0
n = int(input())

for i in range(2, int(sqrt(n)) + 1): #Time Complexity: O(sqrt(n)) 
# for i in range(2,n//2+1):
# for i in range(2, int(num/2)+1):
    if n%i==0:
        flag=1
        break
if n==1:
    print("Neither Prime nor Composite")
else:
    if flag==1:
        print("Composite Number")
    else:
        print("Prime Number")


'''

# Print Prime
import math
def countprime(n):
	for i in range(2,n+1):
		flag=0
		for x in range(2,int(math.sqrt(i))+1):
			if i%x==0:
				flag=1
		if flag==0:
			print(i,end=" ")
				

n=int(input())
countprime(n)

'''