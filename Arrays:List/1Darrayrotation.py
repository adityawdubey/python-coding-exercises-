arr=[1,2,3,4,5,6,7,8,9,10]
k=3

#lfetrotate without using external array/list

# O(n),O(1)
def leftrotate(result,K):
	for i in range(len(arr)-K): #or range(K,len(result)
		result.insert(0,result.pop())
	return result

print(leftrotate(arr,k))
#OR

# O(n),O(1)

def leftrotate(result,K):
	result=result[K:]+result[:K]
	return result
			
print(leftrotate(arr,k))
'''
#OR

# O(n),O(n) #result and  
def leftrotate(result,K): 
	result=result[K:]+result[:K]
	return result




#Rightrotate without using external array/list

def rightrotate(result,K):
	for i in range(K):
		result.insert(0,result.pop())
	return result
	
print(rightrotate(arr,k))




'''
