#WAP to print fibonace series
#e.g. 1 1 2 3

num=int(input("Enter the number :  "))
a=1
b=1
for i in range(1,num+1):
        print(a)
        c=a+b
        a=b
        b=c
