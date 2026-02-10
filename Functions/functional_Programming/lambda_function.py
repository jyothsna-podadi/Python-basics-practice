'''Given 2 list of integers, perform the following operations:

    1.zip(): Combine both lists into one iterable of tuples
    2.filter(): Filter out all elements in list1 that are less than or equal to 2.
    3.map(): Multiply each element of list1 by 2 using  a lambda function'''

list1=list(map(int,input().split()))
list2=list(map(int,input().split()))

zipped=zip(list1,list2)
print(list(zipped))

filtered=filter(lambda x:x<=2,list1)
print(list(filtered))

mapped=map(lambda x:x*2,list1)
print(list(mapped))