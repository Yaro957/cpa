n=input()
ans=""
checker='aAeEiIoOuU'
for char in checker:
    if char in n:
        ans+=char
        break
print(ans)