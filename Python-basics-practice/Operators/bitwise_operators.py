
'''Given three positive integers a,b and c. Your task is to perform some bitwise operations on them as given below
    1. d=a^a
    2.e=c^b
    3.f=a&b
    4.g=c|(a^a)
    5.e=~e'''

a=int(input())
b=int(input())
c=int(input())

d=a^a       #10 ^ 10-->00

e=c^b       #100 ^ 011-->111

f=a&b       #10 & 11-->10

g=c|(a^a)   #100|(010^010)-->100|000-->100

e=~e        #0111--->1000

print(d,e,f,g)
