#multiple herarchical inheritance
'''a class can access
parent 1,parent 2 properties'''


class A():
    def add(self):
        print("class A")

class B():
    def Sub(self):
        print("Class B")

class C(A,B):
    
    def display(self):

      print("CLass C")

obj=C()
obj.display()
obj.add()
obj.Sub()
