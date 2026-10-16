'''

Create a Class Inventory with below attributes:

inventoryId - String
maximumQuantity - int
currentQuantity - int
threshold - int

Write constructor as required.

Create class Solution with main method. 

Implement static method - replenish 
in Solution class.

This method will take an int parameter 
named limit along with the other 
parameter as array of Inventory objects. 
The method will return array of Inventory 
where the threshold attribute 
is less than or equal to the int parameter 
passed.

This method should be called from main 
method and display the id of 
returned objects along with Filling status.

if the threshold is greater than or equal 
to 75 then it should 
print "Critical Filling" as Filling Status. 
If the threshold is 
between 74 to 50 then Filling status 
should be "Moderate Filling", 
else should be "Non-Critical Filling" .

Before calling this method(replenish) in 
the main method, 
use Scanner object to read values for four 
Inventory objects 
referring the attributes in the 
above sequence. 
then, read the value for limit parameter. 
Next call the method replenish and 
display the result. 

Consider below sample input and output:

Input:

1
100
50
40
2
100
50
50
3
100
40
45
4
100
80
25
45

Output:
1 Non-Critical Filling
3 Non-Critical Filling
4 Non-Critical Filling


'''
class Inventory:
    def __init__(self,iid,maxquantity,currquantity,threshold):
        self.iid=iid
        self.maxquantity=maxquantity
        self.currquantity=currquantity
        self.threshold=threshold

class Solution:
    @staticmethod
    def replenish(arr_inv,trgt_param):
        fltr_inv=[]
        for i in arr_inv:
            if i.threshold<=trgt_param:
                fltr_inv.append(i)
        if fltr_inv==[]:
            print("No Data Found")
        else:
            for i in fltr_inv:
                print(i.iid,end=" ")
                if i.threshold>=75:
                    print("Crtical Filling")
                elif i.threshold>74 and i.threshold<50:
                    print("Moderate Filling")
                else:
                    print("Non-Critical Filling")

n=int(input())
lst_inv=[]
for i in range(n):
    iid=input()
    maxquantity=int(input())
    currquantity=int(input())
    threshold=int(input())
    lst_inv.append(Inventory(iid,maxquantity,currquantity,threshold))

trgt=int(input())
Solution.replenish(lst_inv,trgt)