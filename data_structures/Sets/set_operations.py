'''You are given an arr[] of size n. You have to insert all elements of arr[] into a set and return that set. You are also given 
a integer x. if x is found in set then erase it from set and print "Erased x", otherwise, print "Not Found" '''

n=int(input())
arr=list(map(int,input().split()))

s=set(arr[:n])

print(*sorted(s))

x=int(input())
if x in s:
    s.remove(x)
    print(f"Erased {x}")
else:
    print("Not Found")
print(*sorted(s))
