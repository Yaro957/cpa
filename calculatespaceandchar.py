'''Problem Statement
Write a .Python .program . to .compute .the .number
of spaces and characters in a given string

Condition
Ignore all the digits

Explanation
The total number of spaces and all the characters
excluding numbers/digits are computed and printed.

Input
Hello This is ABCD from XYZ city

Output
No of spaces : 6 and characters : 26
'''


a=input()
spac=0
char=0
for i in range(len(a)):
    if a[i]==' ':
        spac+=1
    elif a[i].isalpha():
        char+=1
print(f'No of spaces : {spac} and characters :{char}')
