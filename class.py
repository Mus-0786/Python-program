#inheritance  
class Base:
    def __init__(self,name):
        self.name=name
    def Parent_method(self):
        print("This is a parent class method")

        print(self.name)
class Child(Base):
    def __init__(self,name,age):
           super().__init__(name)
           self.age=age
    def Base_method(self):
        print("This is a child class")
        print(self.age)

obj=Child("Muskan",20)
obj.Parent_method()
obj.Base_method()
