#WAP to count the digit in the no.

num=int(input("Enter the numbers : "))
count=0

while num>0:
    count+=1
    num//=10
print("Total digit is ",count)
