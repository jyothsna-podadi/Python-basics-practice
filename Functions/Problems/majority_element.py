'''Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1'''

def majorityElement(arr):

    count=0
    candidate=None

    for num in arr:
        if count==0:
            candidate=num
            count+=1
        elif num==candidate:
            count+=1
        else:
            count-=1
     
    if arr.count(candidate)>len(arr)//2:
        return candidate
    return -1

arr=list(map(int, input().split()))
print(majorityElement(arr)) 