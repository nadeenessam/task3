n= int (input("Number of element: "))
a= int (input("divided number by: "))
list1= []
for i in range(n):
    element = int(input("enter the element:"))
    list1.append(element)
print("the elements in" , list1, "that are divisible by ", a , " : ")
def division (list,x):
     for i in list:
        if i%a == 0:
           print(i)
division(list1,a)