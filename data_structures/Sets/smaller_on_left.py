'''You are given an array arr[] of n positive integers, the task is to find the greatest element on the left of every element in the array 
which is strictly smaller than itself, if this element does not exist for an index print "-1".'''

import bisect
n=int(input())
arr=list(map(int,input().split()))

seen=[]
result=[]

for x in arr:
    idx=bisect.bisect_left(seen,x)

    if idx==0:
        result.append(-1)
    else:
        result.append(seen[idx-1])
    bisect.insort(seen,x)
print(result)