'''
Question was
Count the occurrence of a target sub-string in the given list of string ..

Condition
If the sub-string present multiple times in a string then count all of them ..

Input-
5
Hello World!
hi I am hello
hello this is Hello
Tcs Xplore
how are you!
hello
Output

4
'''
def counter(lst,trgt):
    c=0
    for i in range(len(lst)):
        c+=lst[i].lower().count(trgt.lower())
    return c
a=int(input())
lst=[]
for i in range(a):
    temp=input()
    lst.append(temp)
target=input()
co=counter(lst,target)
print(co)