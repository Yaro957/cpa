def validatescore(n):
    if n>0 and n<=100:
        return True
    else:
        return False
def findvalidatescore(inpt_scr):
    valid_scr=[]
    for i in inpt_scr:
        if validatescore(i)==True:
            valid_scr.append(i)
    for i in range(len(valid_scr)):
        print(valid_scr[i])
n=int(input())
lst_scr=[]
for i in range(n):
    temp=int(input())
    lst_scr.append(temp)
findvalidatescore(lst_scr)