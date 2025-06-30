#Frequency Arrray 

from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print (Counter(myList))

print (Counter(myList).items())

print(Counter(myList).values())

print(Counter(myList).keys())



'''

5
2 3 3 3 2

1 2 2 2 1

Iteration 1

res=[2]


'''





            





























# https://www.hackerrank.com/challenges/collections-counter/problem

'''
Sample Input 

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output

200

'''

#Solution


# from collections import Counter
# x = int(input())
# shoesizeslist = [int(i) for i in input().split()]
# n = int(input())
# freq = Counter(shoesizeslist)

# print(freq)

# countdict = dict(freq)

# moneyearned = 0
# for i in range(n):
#     size, price = map(int, input().split())
#     if size in countdict:
#         if countdict[size]>0:
#             moneyearned=moneyearned+price
#             countdict[size]=countdict[size]-1
    

# print(moneyearned)

