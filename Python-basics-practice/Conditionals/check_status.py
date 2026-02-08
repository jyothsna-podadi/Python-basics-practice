'''Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Print True for the following cases:
    1. either a or b(not both) is non-negative and the flag is false.
    2. both a and b are negative and the flag is true.'''

a=int(input())
b=int(input())

flag=False

result=True if ((a>=0)^(b>=0)) and not flag or ((a<0) and (b<0) and flag) else False

print(result)