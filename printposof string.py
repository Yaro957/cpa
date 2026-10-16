'''
Write a python code to print the position or index of a given string (taken as input from a user)
from a given list of strings.

The program will take input from the user in the form of a string and will pass the string
as an argument to a function. The function will take the strings as arguments and return the
Position(or index) of the list if the passed string is present in the list, else it'11
return "String not found". If the passed strings are present at multiple indices, in that case,
the function should only return The first index of occurrence.

Considering the above scenario into account, build the logic to print the position of the passed
string from a given list of strings.

Refer to the below instructions and sample input-Output for more clarity on the requirement.

Input:
4
Hello Good Morning
abcd123Fghy
India
Progoti.c
India

Output:
2
'''
def find(lst,stri):
    for i in range(len(lst)):
        temp=lst[i]
        if temp==stri :
            return i
            
    return -1
a=int(input())
b=[]
for i in range(a):
    temp=input()
    b.append(temp)
search=input()
ans=find(b,search)
print(ans)