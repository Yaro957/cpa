
def sep(inpt_string):
    num=""
    str=""
    for char in inpt_string:
        if char.isalpha():
            str+=char
        if char.isdigit():
            num+=char
    ans=[]
    if len(str)>0:
        ans.insert(0,str)
    if len(num)>0:
        ans.insert(1,int(num))
    return ans

stri=input()
ans=sep(stri)
print(ans)