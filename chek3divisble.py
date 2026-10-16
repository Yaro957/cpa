'''Take an integer as input .
Calculate the sum of its digit .
If the sum is divisible by 3 , then print True , else print False .
'''
a=int(input())
temp=a
sum=0
while temp>0:
    x=temp%10
    sum+=x
    temp=int(temp/10)
print(sum)