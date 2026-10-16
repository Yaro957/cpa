'''
Problem Statement
Write a Python program to count both vowels and consonants in
a given string.

Conditions
Only alphabets should be considered for counting

Explanation
The vowels in the given string are e, o and o and so the vowels count
is 3. Likewise, the consonants in the given string are h, l, l,w,r, l
and d and so the count is 7.

Input
Hello World!

Output
Vowels count - 3
Consonants count - 7
'''

str=input()
countv=0
countc=0
vowels='AEIOUaeiou'
for char in str:
    if char.isalpha():
        if char in vowels:
            countv+=1
        else:
            countc+=1
print(f'Vowels count - {countv} \nConsonants count - {countc}')