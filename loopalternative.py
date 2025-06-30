'''
We want you to calculate the sum of squares of given integers, excluding any negatives.
The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
For each test case, calculate the sum of squares of the integers, excluding any negatives, and print the calculated sum in the output.
Note: There should be no output until all the input has been received.
Note 2: Do not put blank lines between test cases solutions.
Note 3: Take input from standard input, and output to standard 

Specific rules for Python solution
Your source code must be a single file, containing at least a main function
Do not use any for loop, while loop, or any list / set / dictionary comprehension

sample ip/op:2
4
3 -1 1 14
5
9 6 -53 32 16

'''

def getpositive(num):
    return num >= 0

def main():
    X = int(input())  # number of elements
    a = list(map(int, input().strip().split()))[:X]
    a = list(filter(getpositive, a))  # list containing positive integers
    squaredlist = list(map(lambda num: num**2, a))  # list containing squares
    print(sum(squaredlist))

# driver code
if __name__ == "__main__":
    tests = int(input())

    def go(upper):
        if(upper > 0):
            go(upper-1)
            main()
    go(tests)

