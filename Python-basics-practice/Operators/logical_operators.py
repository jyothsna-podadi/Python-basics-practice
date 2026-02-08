'''Logical operator and, or, not are used in condition checking. like a and b checks if both a and b are True. First A is checked then b is checked. a or b 
checks if either of a or b is True. If one is True; it doesn't check for other. not a complements the boolean value of a.

In this you basicaaly do:
    1. a and b
    2. a or b
    3. not a'''

a=int(input())
b=int(input())

p= a and b

q= a or b

r= not a

print(p,q,r)