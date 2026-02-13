'''Given two string denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2.'''

def findSum(s1,s2):
    i=len(s1)-1
    j=len(s2)-1
    carry=0

    res=[]

    while i>=0 or j>=0 or carry:
        if i>=0:
            carry+=ord(s1[i])-48
            i-=1
        if j>=0:
            carry+=ord(s2[j])-48
            j-=1
        res.append(chr((carry%10)+48))
        carry//=10
    res="".join(res[::-1])
    res=res.lstrip('0')
    return res if res else '0'

s1=input().strip()
s2=input().strip()

print(findSum(s1,s2))