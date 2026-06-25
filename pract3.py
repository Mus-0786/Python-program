'''value=input("Enter the alphabet: ")
if(value=="a,e,i,o,u"):
    print("the alpha is vowel")
else:
    print("the alphabet is consonant")
'''

value=input("Enter the alphabet: ")
if value=='a' or value=='e' or value=='i' or value=='o' or value=='u':
    print(f"{value} the alpha is vowel")
else:
    print(f"{value} the alphabet is consonant")



'''in operator'''
value=input("Enter the alphabet: ")
if value in "aeiou":
    print(f"{value} the alpha is vowel")
else:
    print(f"{value} the alphabet is consonant")


    
