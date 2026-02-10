'''Given a array arr of integers, return the sums of all subsets in the list. Return the sums in any order.'''

def sumOfSubsets(arr):

    result=[]

    def backtrack(index,current_sum):
        if index==len(arr):
            result.append(current_sum)
            return
        
        backtrack(index+1,current_sum)

        backtrack(index+1,current_sum+arr[index])
    
    backtrack(0,0)
    return result

arr=list(map(int, input().split()))
print(sumOfSubsets(arr))