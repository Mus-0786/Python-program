#WAP to check whether the number is even or onum1=int(input("Enter the number1: "))

'''
num1=int(input("Enter the number1: "))

def check(num1):
    if(num1%2==0):
        print(f"{num1} is even")

    else:
        print(f"{num1} is odd")

check(num1)


'''
# write a function to find the largest of 3 no\

num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
num3=int(input("Enter the number3: "))

def largestno(num1,num2,num3):
    return max(num1,num2,num3)
print("largest number",largestno(num1,num2,num3))
