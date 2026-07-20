#list compression:
'''
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(i**2)
print(list2)
'''
'''using list compression:
list1=[1,2,3,4,5]
list2=[i**2 for i in list1]
print(list2)
'''
'''
for i in range(11):
    if i%2==0:
        print(i)
'''
'''
#using list compresssion
list3=[i for i in range(11) if i%2==0]
print(list3)
'''
#e.g 3
list4=['Muskan','rashmin','Iram']
list5=[i.upper() for i in list4]
print(list5)
