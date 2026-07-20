#SET
'''
1)we can create 2 way by using constructor and using curly braces{}
2)it is mutable in nature
3)no duplicate values are allowed
4)no order is maintained in set
5)does not support indexing
6)we can perform various operation such as union, intersection etc.

'''

set1={10,2,3,4,5}    # create set using the curly braces
print(set1)

 # create set using the set constructor
set2=[10,20,30]
set3=set(set2)
print(set2)

set4={12,345,21,15}
set4.add(50)
print(set4)#using the built in method we can add value

set4.remove(12)#using the built in method we can remove value
print(set4)

set4.discard(201)
print(set4)

#using the built in function we can remove all the value  at a time

set5={12,3,3,21,23,24}
set5.clear()
print(set5)

set6={12,3,3,21,23,24}
set7={12,345,21,15}
union1=set6.union(set7)   # it return all the element from the both side
print(union1)
# intersection return common element from the both side
set6={12,3,3,21,23,24}
set7={12,345,21,15}
union1=set6.intersection(set7)
print(union1)


#difference set contain the element that are in the 1 set but not in the 2
set6={12,3,3,21,23,24}
set7={12,345,21,15}
union1=set6.difference(set7)
print(union1)

#difference set contain the element that are in either in any set but not both
set6={12,3,3,21,23,24}
set7={12,345,21,15}
union1=set6.symmetric_difference(set7)
print(union1)

#subset
set6={12,3,3,21,23,24}
subset1={20,3}
is_subset=subset1.issubset(set6)
print(is_subset)







