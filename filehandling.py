#file handling
#file is used to store the data
#open(): file name,access mode:used to open the file
#w represent over the write
#a is used append mode
#close() is used to explicitly close the file 
'''
var=open("file_name.txt","w")
if var:
    print("File Created successfully")
var.close()
'''
'''
#we can close the file automatically using with
with open("file1.txt","w") as file:
    file.write("file 1 is exist")
with open("file1.txt","r") as var:
    reading=var.read()
print(reading)
'''
''''
#in their multiple line in the file we can read file line by line using strip
with open("file1.txt","r") as var:
    for i in var:
        print(i.strip())'''
'''
with open("file1.txt","a") as file:
    file.write("file 1 is exist")
'''


#csv file
import csv
with open("student.csv","r") as csv_reader:
    content=csv.reader(csv_reader)
    header=next(content)
    for i in content:
        print(i[0],i[1],i[2])

'''
list1=[[1021,Riya Sharma,Bhopal Madhya Pradesh
1022,Harsh Agarwal,Indore Madhya Pradesh
1023,Sahil Khan,Kochi Kerala]]'''
