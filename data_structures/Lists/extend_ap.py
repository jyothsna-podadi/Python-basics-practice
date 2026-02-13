'''you are given an array arr[] whose elements form an arithmetic progression(AP). your task is to determine 
the next three numbers in the progression and return a new array containing the original sequence along with these 
three additional term.'''

arr=list(map(int,input().split()))

diff=arr[1]-arr[0]

last=arr[-1]

for _ in range(3):
    last+=diff
    arr.append(last)
    
print(arr)