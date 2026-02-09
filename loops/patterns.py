'''Given an integer n, write a program to print the hallow square of size n using('*')'''

n=int(input())

for i in range(n):
    
    if (i==0 or i==n-1): 
        print("* "*n,end="")
    
    else:
        print("*"+" "*(2*n-3)+"*",end="")
    print()