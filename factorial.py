#WAP to calculate the factorial no. using while loop
# e.g.  5=5*4*3*2*1

num=int(input("Enter the No. : "))
fact=1
while num>=1:
    fact=fact*num
    num-=1
print("Factorial is=",fact)
