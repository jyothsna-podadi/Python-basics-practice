'''You are given a list of students names(keys) and their corresponding marks(values).
the task is to do operations as described below:
    1.k key, v value: Insert given key k and value in the dictionary, print "Inserted" after inserting
    2.d key: delete the entry for a given key d and print "Deleted" if the key to be deleted is present, else print "-1".
    3.p key: Print marks of a given key p in statements as "Marks of {student_name} is: {marks}". if key is not present 
      print -1.'''

keys=input().split()
values=list(map(int,input().split()))

my_dict=dict(zip(keys,values))

k,v=input().split()

#Inserting 
my_dict[k]=int(v)
print("Inserted")

#deleting
d=input().strip()

if d in my_dict:
    del my_dict[d]
    print("Deleted")
else:
    print(-1)

#print marks

p=input().strip()

if p in my_dict:
    print(f"Marks of {p} is: {str(my_dict[p])}")
else:
    print(-1)