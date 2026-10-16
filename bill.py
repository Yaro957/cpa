'''
Create a class Bill with below attributes:

billNo- int
name - String
typeOfConnection - String
billAmount - double
status - boolean

where billNo is the bill number, name 
is the name of the customer, 
typeOfConnection is the type of the 
connection (prepaid, postpaid), 
billAmount is the bill amount and 
status is whether the bill is paid 
or not (if paid then value is TRUE 
else value is FALSE). 

The above attributes should be private, 
write getters, setters and 
parameterized constructor as required. 

Create class Solution with main method.
Implement two static methods - 
findBillWithMaxBillAmountBasedOnStatus 
and getCountWithTypeOfConnection 
in Solution class.

findBillWithMaxBillAmountBasedOnStatus method:
This method will take an array of 
Bill objects and a boolean parameter 
as parameters. 

The method will return bill object 
array in ascending order of 
their bill number from the array of 
Bill objects whose bill 
Amount is maximum in the array with 
the status attribute that 
matches with the input parameter.

If no Bill with the given status is 
present in the array 
of Bill objects, then the method should 
return null.

getCountWithTypeOfConnection method:
This method will take two input 
parameters - array of Bill
objects and string parameter ( for type 
of connection).
The method will return the count of bills 
from array of bill 
objects for the given type of connection.
If no bill with the given type of 
connection is present in 
the array of bill objects, then 
the method should return 0.


Note :

Two bill object can have the same 
bill amount.
All the searches should be case insensitive. 

The above mentioned static methods 
should be called from the main method.

For findBillWithMaxBillAmountBasedOnStatus 
method - The main method 
should print the billNo followed by # and 
name from the returned 
Bill object array if the returned 
value is not null.

If the returned value is null then 
it should print 
"There are no bill with the given status".


For getCountWithTypeOfConnection method - 
The main method should 
print the count of bills as it is, if the 
returned value is greater than 0,  
otherwise it should print 
"There are no bills with given type of connection".


Before calling these static methods in 
main, use Scanner to read the 
number of object and objects to read 
the values of Bill objects 
referring attributes in the above 
mentioned attribute sequence. 

Next, read the value for status and 
typeOfConnection.


Consider below sample input and output:
Input:

4
111
Aman Mittal
Prepaid
914.25
true
222
Rekha Kumar
Prepaid
1425.75
false
333
Samyra Gupta
Prepaid
1305.00
true
444
Mohit Saxena
Postpaid
1300.50
false
false
Prepaid

Output:

222#Rekha Kumar
3
'''

class Bill:
    def __init__(self,bno,name,toc,billamount,status):
        self.__bno=bno
        self.__name=name
        self.__toc=toc
        self.__billamount=billamount
        self.__status=status
    def get_bno(self):
        return self.__bno
    def get_name(self):
        return self.__name
    def get_toc(self):
        return self.__toc
    def get_billamount(self):
        return self.__billamount
    def get_status(self):
        return self.__status


class solution:
    @staticmethod
    def findBillWithMaxBillAmountBasedOnStatus(arr_bill,value):
        lst=[]
        for i in arr_bill:
            if i.get_status()==value:
                lst.append(i.get_billamount())
        if lst==[]:
            print("There are no bill with the given status")
        else:
            for i in arr_bill:
                if i.get_status=="True":
                    if max(lst)==i.get_billamount():
                        print(f"{i.get_bno()}#{i.get_name()}")

    def getCountWithTypeOfConnection(arr_bill,trgt_type):
        count=0
        for i in arr_bill:
            if i.get_toc().lower()==trgt_type.lower():
                count+=1
        if count==0:
            print(0)
        else:
            print(count)

n=int(input())
lst=[]
for i in range(n):
    bno=int(input())
    name=input()
    toc=input()
    billamount=float(input())
    status=input()
    lst.append(Bill(bno,name,toc,billamount,status))
trgt_status=input()
trgt_toc=input()
solution.findBillWithMaxBillAmountBasedOnStatus(lst,trgt_status)
solution.getCountWithTypeOfConnection(lst,trgt_toc)
