# from tkinter.font import names


# class parrot:
#     ins= "bird"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj1= parrot("blue",22)
# obj2= parrot("red",24)

# print(f"color {obj1.name}, age {obj2.age}")


class parrrrot:
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def color(self,flat):
        print("its flat of 2nd floor",self.name,flat)

    def note(self):
        print("no arg")


obj3= parrrrot("green",24)

obj3.color("happy")
obj3.note()

class Incap:
    def __init__(self):
        print("this is parnent")

    def floor(self,add):
        print("floor test in maha", add)

    def low(self):
        print("how its low")

class Child(Incap):
    def __init__(self):
        super().__init__()
        print("this is super")

    def small_child(self):
        print("its small child")


obj4 = Child()
obj4.floor("yes")
obj4.low()
