'''Juggler Sequence is a series of integers in which  the first term starts with positive integer number a and the remaining terms are generated from 
the immediate previous term using the recurrence relation'''

def jugglerSequence(a):

    seq=[a]

    while a!=1:
        if a%2==0:
            a=int(a**0.5)
        else:
            a=int(a**1.5)
        
        seq.append(a)
    return seq

a=int(input())
print(jugglerSequence(a))