'''
1. Sort the Summary
Given an array of integers, create a 2-dimensional array where the first element is a distinct value from the array and the second element is that value's frequency within the array. Sort the resulting array descending by frequency. If multiple values have the same frequency, they should be sorted ascending.
Example
arr = (3, 3, 1, 2, 11
• There are two values, 3 and 1, each with a frequency of 2, and one value 2 with a frequency of 1:
[[3, 2], [1, 2], [2, 11]
• Sort the 2-dimensional array descending by frequency: [I3,21, [1, 21, [2, 11]
• Sort the 2-dimensional array ascending by value for values with matching frequencies: [[1,2], [3,
21, [2, 111
Function Description
Complete the function groupSort in the editor below.
groupSort has the following parameter(s):
int arr[n): an array of integers
Returns:
int[n][2]: a 2-d array of integers sorted as described

'''

from collections import Counter

def groupSort(arr):
    freqarray=Counter(arr)
    return sorted(freqarray.items(), key=lambda x:(x[1], -x[0]),reverse=True)


# import collections

# arr = [3,3,1,2,1]
# freq = collections.Counter(arr)
# print(freq)
# l = [[k,v]for k,v in freq.items()] 
# sorted_freq = sorted(sorted(l, key = lambda x : x[0]), key = lambda x : x[1], reverse = True) 
# print(sorted_freq)