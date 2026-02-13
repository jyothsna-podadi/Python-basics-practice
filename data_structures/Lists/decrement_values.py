'''You are given a list that contain integers. You need to decrement each element of the list by 1 and return the list'''

def decrement(arr):
    l=[]
    for i in arr:
        l.append(i-1)
    return l

arr=list(map(int,input().split()))
print(decrement(arr))