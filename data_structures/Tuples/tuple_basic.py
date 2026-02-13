'''You are given a tuple numbers that contain integers. You need to return  a tuple containing doubles of given numbers.'''

arr=tuple(map(int,input().split()))

for i in arr:
    print(i*2,end=" ")
