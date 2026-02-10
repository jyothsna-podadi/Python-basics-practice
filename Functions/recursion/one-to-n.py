'''Given an integer n, print numbers  from 1 to n without using loops'''

def printTillN(n):
    
    if n==0:
        return
    
    printTillN(n-1)
    print(n,end=" ")

n=int(input())
printTillN(n)

