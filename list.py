'''List
It is store different type of data
It is muttable
it can store heterogenuos data(different type)

Creating the List'''
'''
var=['Muskan',1,2,3.0,True]
print(var)

#accessing the 3.0
print(var[4])
#accessing 3.0 using print()/slice
print(var[3:4])
#we can modify the list
var[3]=3.5
print(var)

#to add the value in end of list
var1=['Muskan',12,32,3.0,True]
print(var.append("Apple"))
print(var)
#length of the list
var2=['M',2,3,3.0,True]
print(len(var2))


#insert function is used to insert the item at the specified position
list3=['Name',5,2.5,232]
list3.insert(3,10)
print(list3)

#remove() is used to remove the fisrt occurances of the element

list4=['name',2,65,3.0,2]
list4.remove(2)
print(list4)
#['name', 65, 3.0, 2]

#pop is used to remove and return the value
list5=['muskan',3,65,132]
a=list5.pop(3)
print(a)
print(list5)
#['muskan', 3, 65]

#index() its return the fisrt occurances of sepecified value
list6=['m' ,4 ,6 ,3 ,56.6 , 5]
print(list6.index(4))

#count return the number of types of the values appear in the list
list7=[2,4,56,7,3,6,3,2,2,4,5,2,2]
print(list7.count(2))#5

#sort() is used to to sort the value in ascending
list8=[2,4,56,7,3,6,3,2,2,4,5,2,2]
list8.sort()
print(list8)

# reverse()
list8=[1,2,4,6,7,823]
list8.reverse()
print(list8)'''
'''
#copy() is used to which is create the copy/shadow
list9=[1,2,4,6,7,823]
list10=list9.copy()
print(list10)
#using slice() and sort() in desecdeng order
list12=[24,565,2.7,232,76]
list12.sort()
print(list12[::-1])
#using sorted
list13=[24,65,2.7,32,76]
des=sorted(list13,reverse=True)
print(des)#[76, 65, 32, 24, 2.7]

#traversing the list
list14=[3,32,43,6,3]
for i in list14:
    print(i)

#using  for while loop
list15=[3,32,43,6,3]
i=0
while len(list14)>i:
    print(list14[i])
    i+=1

#

list16=[2,5,24,13,32,4]
for index,value in enumerate(list16):
    print(index,value)

'''
#wap to find even or odd of list=[1,2,3,4,5,6,7]
#WAP to find the largest number from the list
#WAP to find 2nd largest element list=[20,35,45,22,68]
#except the element from the user and check whether the list exist or not


list=[1,2,3,4,5,6,7]
for i in list:
    if i%2==0:
        print(list)
