#Dictionar compression
#convert list into dictionary using the list compression

list1=[1,2,3,4,5]
dict1={var:var**2 for var in list1}
print(dict1)

#e.g key value pair
'''
count=int(input("Enter the Student details: "))
var={input("Enter the Studentt Name"):int(input("Enter the Age: ")) for _ in range(count)}
print(var)
'''
Product_count=int(input("Enter the Product details: "))
var={input("Enter the Product Name: "):int(input("Enter the Price: ")) for _ in range(Product_count)}
print(var)
