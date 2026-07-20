''' Overriding method= in which child class provides its  implementation of methods
that is already in parent class
child class have same and parameter as the method in parent class
WHY it is used:compile time overloading'''

class Parent:
    def __init__(self):
        print("Parent class constructor")
        
    def display(self):
        print("parent class")
        
        
class Child(Parent):
    def __init__(self):
        print("Child class constructor")
        super().__init__()
    def display(self):       #self is used to refer the current class obj
        print("Child Class")
        super().display()    #it is used access the parent class


        
obj=Child()
obj.display()
