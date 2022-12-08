# Python is a general purpose high level language
# Guido van rossum is the inventor

# features: It is functional, modular, object oriented, scripting language

# It can be used to create desktop, web based, develop database, gaming appln.

# printing is very simple
# print("hello world")

# Declaring variable, and its type
# x = 'a'
# print(x)
# print(type(x))

# sum of 2 number
# a=10
# b=13
# print(a+b)
#
# a=20
# b=13
# print(a-b)
#
# a=20
# b=2
# print(a*b)
#
# a=20
# b=2
# c=2
# print(a/b+c)

# Identifiers: It is used for identification. it can be variable, class or method name.

# alphabets(u/l), digits  and underscore can be used.

# It cannot be special character, cannot start with numbers, keywords and case sensitive.

# Class, objects and reference variable

# class = blue print/plan/model for objects, which contain complete information.
# objects = Physical existance of class.
# Ex: features of TV is class and TV we can make it as object
# class and oject are like one to many
# each objects has its own properties are specified by variables and behaviour specified by methods.
# Types of variable: Instance: Object level variables.
# static variable: class level variables
# local variables - method level variables.
# Types of methods - Instance -
# class -
# static methods -

# Reference variable - it is used to refer objects. Also we can invoke functionality of object.
# single object can have multiple reference variable.

# class Student:
#     def __init__(self):---->constructor
#         self.name = 'vinyas'
#         self.rollno = 101
#         self.subject = 'Maths'
#         self.marks = 100
#     def talk(self):
#         print("My name is:",self.name)
#         print("roll no is:",self.rollno)
#         print("subject is:", self.subject)
#         print("marks is:", self.marks)
# s = Student()
# # print(s.rollno)
# # print(s.name)
# # print(s.subject)
# # print(s.marks)
# s.talk()

# Constructor = it is a special method, where we call using __init__().whenever we create object
# it will call automatically no need to call explicitly. Per object constructore will be executed only once.
# purpose - it helps in initializing ()and declaring the instance variable
# self - to refer current object or accessing the object.
# constructor should take atleast one argument.
# ex:
# class student():
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
# s1 = student("yash",101,90)
# s1.__init__("yashu",102,100)
# print(s1.name)
# print(s1.rollno)
# print(s1.marks)

# Constructer overloading = multiple constructor with same name but different arguments types. its not possible in
# python. if there are multiple constructor only last constructor will be executed.
# class Test:
#     def __init__(self):
#         print("hello")
#
#     def __init__(self,x):
#         print("number is",x)
#
# t = Test(10)

# constructor overriding =



# Functions: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# write code only once and call the same multiple times, main advantage is resusibility

# dev calculate(a,b):
#     print("The sum of a and b",a+b)
#     print("The sum of a and b", a-b)
#     print("The sum of a and b", a*b)
# calculate(20,10)
# calculate(100,90)

# Inheritance - Inheritance allows us to define a class that inherits all the methods and properties from another
# class. Parent class is the class being inherited from, also called base class. Child class is the class that
# inherits from another class, also called derived class.
# Advantages: Reusibility of the code and extension of funtionality.
# Types: Single Inheritance: process of inheriting properties from one parent class to one child.
# ex: class P:
#     def m1(self):
#           print("hi i am parent")
# class C(P):
#     def m2(self):
#           print("Hi i am child of parent")
#
# r=C()
# r.m1()
# r.m2()

# class garrage():
#     def Maruthi800(self):
#         print("Service total amount 10k")
# class painting(garrage):
#     def Nippon(self):
#         print("Paint cost 5k")
#
# Total = painting()
# Total.Maruthi800()
# Total.Nippon()

# Multi level: process of inheriting properties from one parent class to one child where child will become
# parent of next child.

# class Testyantra():
#     def RMG(self):
#         print(" RMG take care of bench")
# class Tyss(Testyantra):
#     def MQAS(self):
#         print("MQAS takes of project")
# class testyantra(Tyss):
#     def HR(self):
#         print("HR Takes care of HR activities")
# TTSSPL=testyantra()
# TTSSPL.MQAS()
# TTSSPL.RMG()
# TTSSPL.HR()

# hierarchial: process of inheriting properties from one parent for multiple childs.

# class colorskannada():
#     def Ayogya(self):
#         print("It is a movie")
# class serial(colorskannada):
#     def kannadathi(self):
#         print("it is a famous serial")
# class realityshow(colorskannada):
#     def rajarani(self):
#         print("its a famous reality show")
# TV = realityshow()
# TV.Ayogya()
# TV.rajarani()
# print("only its and its parent methods are available")
# TV1 = serial()
# TV1.Ayogya()
# TV1.kannadathi()

# multiple: single child inheriting properties of multiple parents.

# class P():
#     def M1(self):
#         print("Welcome")
# class P1():
#     def M1(self):
#         print("to")
# # class c(P1,P):pass
# class c(P1,P):
#     def M1(self):
#         print("hello")
# r = c()
# r.M1()

# hybrid: mixture of all the inheritance.

# Generators: Python generators are a simple way of creating iterators.
# It is responsible to generate sequence of values. It makes use of yield keywords.
# difference between generator and iterator
# A process that is repeated more than one time by applying the same logic is called an Iteration.
# It is another way of creating iterators in a simple way where it uses the keyword “yield”
# instead of returning it in a defined function. Generators are implemented using a function.

# Advantages: Memory utilization, performance improvisation,easy to use
# generators are best suiltable for large data handling.
# webscrapping or scrolling
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g = mygen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# program for countdown
# import time
# def countdown(num):
#     print("count down starts now")
#     while num>0:
#         yield num
#         num=num-1
# values = countdown(10)
# for x in values:
#     print(x)
#     time.sleep(2)

# to generate first n numbers
import time

# def firstn(num):
#     print("first n numbers are")
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# values = firstn(10)
# for x in values:
#     print(x)
#     time.sleep(1)

# fibonacci numbers
# import time
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b=b,a+b
# values = fib()
# for x in values:
#     if x>50:
#         break
#     print(x)
#     time.sleep(1)

# Exceptional Handling: Handling the different types of error. this can be utilized or defining alternative way to continue normal flow of the program.
# only for run time errors.
# exception: unwanted unexpected event that disturbs normal flow of program
# 1.syntax error - ex:paranthesis missing or colon missing
# 2.run time error - logical mistakes, arithemetic error,
# invalid input (zero division error,type casting error(value error),file not found)
# os error(file not found error, interrupted error, time out error),look up error.
# memory issues
# objective/purpose: for graceful/normal termination of program we should not block the flow and miss anything.
# example:
# class menu():
#     try:
#         # risky code
#         def div():
#             x = 10
#             y = 0
#             print("answer is:", x / y)
#     # defining alternative way/code
#     except ZeroDivisionError:
#         print("it is not divisble by 0")
# menu()
# try except with multiple blocks
# ex:
# try:
#     x = int(input("Enter x value:"))
#     y = int(input("Enter y value:"))
#     print("x/y is:",x/y)
#
# except ZeroDivisionError:
#     print("number not divisble by 0")
#
# except SyntaxError:
#     print("Syntax missing")
# clean up code(close db) cannot be used in try block since rest of the code will not be executed
#     ,it cannot be used in except block since if there are no exception also except block will be
# if executed:
# so always make utilization of finally block
# ex:
# try:
#     print(10/3) to maintain source code
# except ZeroDivisionError:
#     print("not divisable") to maintain exception
# finally:
    # print("finally") to maintain cleanupcode

# try:
#     print(10/0)
# except SyntaxError:
#     print("not divisable")
# finally:
#     print("finally")

# finally
# cleanup code will be accepted

# os._exit(0)
# 0 means normal termination
# non 0 means abnormal termination

# Python JSON --> Java script object notation.
# process of converting python object to network supported form or file form is serialization
# most commonly used message format for applications irrespective of language
# it will be human readable form
# it is very similar to python dict object
# it is light weight and less memory to store the data.
# Java script object contains a group of key avalue pairs
# dumps() = it serializes python dict object to json string.
# dump = it converts python dict object to json and write the same to specified file.
# deserialization
# loads()=converting json string to python dict.
# load


# function aliasing - for existing function we can define another name.
# ex:
# def wish(name):
#     print("Good morning")
# greeting = wish
#
# greeting("yashu")
# wish("anu")
# del wish
# greeting('rocky')

# Nested function - function within a function
# a function can return another function

# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     print("I am outer function2")
#     inner()
# outer()

# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     print("I am outer function2")
#     return inner
# outer()

# def outer():
#     print("I am outer function")
#     def inner():
#         print("I am inner function")
#     print("I am outer function2")
#     return inner
# i = outer()
# i()

# filter is an function for filtering purpose based on condition
# syntax: filter(function,sequence)

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,8]
# l2=list(filter(even,l))
# print(l2)

# map - its is a function which maps the condition for sequence of elements

# def squareit(x):
#     return x*x
# l = [1,2,3,4,5,6]
# l2 = list(map(squareit,l))
# print(l2)

# reduce  - reduce all the elements into single elements

# from functools import reduce
# def simplify(a,b):
#     return a*b
# l = [1,2,3,4,5]
# l2 = reduce(simplify,l)
# print(l2)

# Decorators - It is a function takes input function as argument and perform some enhancement and return
# enhanced output function.

# def decor(func):
#     def inner():
#         print("#*"*20)
#         print("123456")
#         print("0,9,8,7,6")
#         func()
#         print("#*" * 20)
#     return inner
# @decor
# def f1():
#     print("Welcome to Bigboss")
# f1()

# def decor(func):
#     def inner(name):
#         if name == 'Anu':
#             print("^" * 20)
#             print("hell0", name, "Good morning")
#             print("Welcome to UK")
#             print("^" * 20)
#         else:
#             func(name)
#     return inner
# @decor
# def f1(name):
#     print("hell0",name,"Good morning")
# f1('Anu')

# def multiply(func):
#     def inner(a,b):
#         print("*"*20)
#         print("Hello kids, come will multiply")
#         print("a*b is:")
#         func(a,b)
#         print("*" * 20)
#     return inner
#
#
# @multiply
# def add(a,b):
#     print(a*b)
# add(2,3)

# without decor
#
# def decor(func):
#     def inner(a,b):
#         print("('')"*20)
#         print("Value of a is:",a)
#         print("Value of b is",b)
#         print("The total sum of {} and {} is {}".format(a,b,a+b))
#         print("('')" * 20)
#     return inner
#
# def add(a,b):
#     print("sum of a and b is:",a+b)
# add(10,20)
#
# enhanced_func = decor(add)
# enhanced_func(100,200)

# decorator chaining

# decorator within decorator

# def decor1(func):
#     def inner():
#         print("first function")
#     return inner
# def decor2(func):
#     def inner1():
#           print("second function")
#     return inner1
#
#
# @decor2
# @decor1
# def f1():
#     print("Lets print original function")
# f1()

# def decor1(func):
#     def inner1():
#         x=func()
#         return x*x
#     return inner1
# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
# @decor1
# @decor
# def num():
#     return 10
# print(num())

# super()method - helps in calling from parent class. main use code reusability.
# Mainly usable in inheritance

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self,phno,marks,subject):
        super().__init__(self,name,age)
        self.phno = phno
        self.marks = marks
        self.subject = subject

class Teacher(person):
    def __init__(self,name,age,subject,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.subject = subject


m1=person("rakesh",50)
m = student(990876767,101,"kannada")
print(m.name)
print(m.age)
print(m.phno)
print(m.marks)
print(m.subject)






# constructor

