# abstract method: even we donot no implementation still we are declaring a method.
# only declaration and no implementation, where child class should give implementation.
# ex:

# from abc import *
# class abs():
#     @abstractmethod           #its the decorator, which is available inside abc(abstract base class) module
#     def example(self):pass
#         # print("hello")
# t = abs()
# t.example()

# abstract class
# if class has partial implementation

# ex:

# from abc import ABC, abstractmethod
#
#
# class Polygon(ABC):
#
#     @abstractmethod
#     def noofsides(self):
#         pass
#
#
# class Triangle(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
#
# class Pentagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 5 sides")
#
#
# class Hexagon(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 6 sides")
#
#
# class Quadrilateral(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 4 sides")
#
#
# # Driver code
# R = Triangle()
# R.noofsides()
#
# K = Quadrilateral()
# K.noofsides()
#
# R = Pentagon()
# R.noofsides()
#
# K = Hexagon()
# K.noofsides()






















