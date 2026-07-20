class Parent():
    def P_method(self):
        print("Parent Class")

class Child1(Parent):
    def C1_method(self):
        super().P_method()
        print("Child Class")

class Child2(Parent):
    def C2_method(self):
        print("Child Class 2")

obj=Child1()
obj.C1_method()
obj2=Child2()
obj2.C2_method()
