#WAP to check whether the armstrog number or not


num=int(input("Enter the No. : "))
temp=num
digit=0
arm=0

while temp>=1:
    digit=temp%10
    arm=arm+(digit**3)
    temp//=10
if num==arm:
    print("Armstrong number")

else:
     print("Not a Armstrong number")
