'''Given a number n, find the value of n raised to power of its own reverse.'''

def powerReverse(n):
    temp=n
    rem=0
    while temp>0:
        digit=temp%10
        rem=(rem*10+digit)
        temp//=10
    return n**rem
n=int(input())
print(powerReverse(n))
