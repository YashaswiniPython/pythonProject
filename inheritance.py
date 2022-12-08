#Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


# single inheritance
# class A:
#     def test(self):
#         print("i am A")
#
# class B(A):   #single inheritance
#     def test1(self):
#         print("i am B")
#
# i = B()
# i.test()

# multilevel:
# class Employees():
#
#     def Name(self):
#         print
#         "Employee Name: Khush"
#
#
# class salary(Employees):
#     def Salary(self):
#         print
#         "Salary: 10000"
#
#
# class Designation(salary):
#     def desig(self):
#         print
#         "Designation: Test Engineer"
#
#
# call = Designation()
# call.Name()
# call.Salary()
# call.desig()

# class A:
#     def test(self):
#         print("i am A")
#
# class B(A):
#     def test1(self):
#         print("i am B")
#
# class C(B):
#     def test2(self):
#         print("i am C")
#
# class D(C):
#     def test3(self):
#         print("i am D")
#
# i = D()
# i.test1()

# hierarchial inheritance
# class A:
#     def test(self):
#         print("i am A")
#
# class B(A):
#     def test1(self):
#         print("i am B")
#
# class C(A):
#     def test2(self):
#         print("i am C")
#
# class D(A):
#     def test3(self):
#         print("i am D")
#
# i = D()
# i.test()

# multiple inheritance
# single child multiple parents
#
# class Class1:
#     def m(self):
#         print("In Class1")
#
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
#
# class Class4(Class2, Class3):
#     pass
#
#
# obj = Class4()
# obj.m()
# class A:
#     def test(self):
#         print("i am A")
#
# class B:
#     def test1(self):
#         print("i am B")
#
# class C:
#     def test2(self):
#         print("i am C")
#
# class D(B,A):
#     def test3(self):
#         print("i am D")
#
# i = D()
# i.test1()


























