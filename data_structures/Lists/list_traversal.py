'''You are given a list that contain integers. You need to print the elements of the list with a space between them.'''

arr=list(map(int,input().split()))

for i in arr:
    print(i,end=" ")