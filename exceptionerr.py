#Eception Handling
'''Exception is the error that occur during the execution of theprogram and which stop the execution of the
the program and display the error
types of Exception:
Indexerror,typeerror,valueerror,filenotfound error,zero division error
you can use multiple except block after the try block'''
'''
try:
    ans=2/0
except ZeroDivisionError:
    print("You devide the no by Zero")
'''
'''
num=int(input("Enter the number:"))
try:
    nom=20/num

except ValueError:
    print("No is valid")
    
except ZeroDivisionError:
    print("You devide the no by Zero")
else:
    print(nom)
'''

