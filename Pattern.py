#Lower Triangle 
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# pattern=[[j for j in range(1,6) if i >= j] for i in range(1,6) ]
# print("\n".join(" ".join(map(str,line))for line in pattern))

# for i in pattern:
#     for j in i:
#         print(j, end=" ")
#     print()

# pattern=[[str(j) for j in range(1,6) if i >= j] for i in range(1,6) ]
# for i in pattern:
#     print(" ".join(i))



#Diamond
'''
        *        
      * * *      
    * * * * *    
  * * * * * * *  
* * * * * * * * *
  * * * * * * *  
    * * * * *    
      * * *      
        *    
'''
n=13
pattern=[[" " if (i+j<n//2) or (j-i>n//2) or (i-j>n//2) or (i+j>(3*n-3)//2) else "*" for j in range(n)] for i in range(n)]
print("\n".join(" ".join(map(str,line))for line in pattern))

