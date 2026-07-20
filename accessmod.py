#access modifier
'''
Encapsulation means binding data and function together that operate as a single unitcalled as a class
Encapculation is used to handling the data

public: accessible anywhere
private:the data member that indicateby __()
protected:its access by sub classes and it indicate by _()

'''



class Student:
    def __init__(self,name):
        self.__name=name
    def display(self):
        print(self.__name)
obj=Student("Muskan")
obj.display()
