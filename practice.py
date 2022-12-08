# import time
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for x in fib():
#     if x>100:
#         break
#     print(x)
#     time.sleep(1)


# import time
# def countdown(num):
#     print("countdown starts now:")
#     while num>0:
#         yield num
#         num = num-1
# values=countdown(10)
# for x in values:
#     print(x)
#     time.sleep(1)
# import time
#
# import time
# def firstn(num):
#     n=1
#     while n<num:
#         yield n
#         n=n+1
# values = firstn(10)
# for x in values:
#     print(x)
#     time.sleep(1)

# inheritance

# single:
# class A():
#     def m1(self):
#         print("hello")
# class B(A):
#     def m2(self):
#         print("good morning")
# s = B()
# s.m1()

# multilevel:
# class A():
#      def m1(self):
#          print("hello")
# class B(A):
#      def m2(self):
#          print("Anu")
# class C(B):
#     def m3(self):
#         print("BFF")
#
# s = C()
# s.m1()

# hierachial
#
# class A():
#     def m1(self):
#         print("hello")
# class B(A):
#     def m2(self):
#         print("Welcome")
# class C(A):
#     def m3(self):
#         print("to TYSS")
# s = C()
# s.m3()

# multiple

# class A():
#     def m1(self):
#         print("hello")
# class B():
#     def m2(self):
#         print("Welcome")
# class C(B,A):
#     pass
#
# s = C()
# s.m1()
# s.m2()

# import time
# def countdown(num):
#     print("countdown starts now")
#     while num > 0:
#         yield num
#         num = num -1
# values = countdown(10)
# for x in values:
#     print(x)
#     time.sleep(1)

# import time
# def firstn(num):
#     n = 1
#     while n<=num:
#         yield n
#         n = n+1
# values = firstn(10)
# for x in values:
#     print(x)


# fib
# import time
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b=b,a+b
# val = fib()
# for x in val:
#     if x>20:
#         break
#     print(x)
#     time.sleep(1)

# function aliasing

# def wish(name):
#     print("Good morning")
# greet = wish
# # wish('yashu')
# del wish
# greet('anu')

# Nested fucntion
# def outer():
#     print("I am outer function")
#     def inner():
#         print("i am inner function")
#     return inner()
# outer()

# Filter
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l = [1,2,4,4,56,70]
# l2 = list(filter(even,l))
# print(l2)

# map
# def sum(a):
#     return a*a
# l=[1,2,3,4,5]
# l2 = list(map(sum,l))
# print(l2)

# reduce
# from functools import reduce
# def red(a,b):
#     return a+b
# l = [1,2,4,5,6]
# l2 = reduce(red,l)
# print(l2)

# decorators

#
# def decor(func):
#     def inner(a,b):
#         print("$"*25)
#         print("sum of {} and {} is {}".format(a,b,a+b))
#         print("$" * 25)
#     return inner
#
# # @decor
# # use with decor
# def add(a,b):
#     print("sum of a,b is:", a+b)
# enhanced = decor(add)
# # ("above use without decor")
# # add(10,20)
# enhanced(30,20)

# def gen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#     yield 'D'
# g = gen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# countdown
# import time
# def countdown(num):
#     while num>0:
#         yield num
#         num = num-1
# g = countdown(10)
# for x in g:
#     print(x)
#     time.sleep(1)

# import time
#
# def countup(num):
#     while num<20:
#         yield num
#         num = num+1
# g = countup(10)
# for x in g:
#     print(x)
#     time.sleep(1)

# n numbers
import time
#
#
# def nn(num):
#     print("The firts 10 numbers are")
#     n = 1
#     while n<=num:
#         yield n
#         n=n+1
# val = nn(10)
# for x in val:
#     print(x)
#     time.sleep(1)

# def countdown(num):
#     while num > 0:
#         yield num
#         num = num-1
# val = countdown(10)
# for x in val:
#     print(x)
#     time.sleep(2)

# def nnumber(num):
#     print("The numbers are:")
#     n = 1
#     while n<=num:
#         yield n
#         n = n+1
# n = nnumber(10)
# for x in n:
#     print(x)
#     time.sleep(2)

# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# val = fibonacci()
# for x in val:
#     if x>20:
#         break
#     print(x)
#     time.sleep(2)

# map

# def square(n):
#     return n*n
# l = [1,2,4,5,6,7]
# l1 = list(map(square,l))
# print(l1)

# reduce

# from functools import reduce
#
# def mul(a,b):
#     return a*b
# l = [1,2,3,4,5,6]
# l1 = reduce(mul,l)
# print(l1)

from functools import reduce
# def multipl(a,b):
#     return a*b
# l = [1,2,3,4,5]
# l1 = list(map(multipl,l))-map
# l1 = reduce(multipl,l)-reduce
# print(l1)

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l = [1,2,3,4,5,10,20,30]
# l1 = list(filter(even,l))
# print(l1)

# def countdown(num):
#     while num>0:
#         yield num
#         num = num-1
# val = countdown(10)
# for x in val:
#     print(x)
#     time.sleep(1)
#
# def count(num):
#     print("The numbers are")
#     n=1
#     while num<0:
#         yield num
#         num = num-1

# Encapsulation:


# decorator
#
# def decor(func):
#     def inner(a,b):
#         print("*"*40)
#         print("enter the value for a",a)
#         print("enter the value for b",b)
#         print("The value of {} and {} is {}".format(a,b,a+b))
#         print("*" * 40)
#     return inner(10,20)
#
# # @decor
# def add(a,b):
#     print(a+b)
# without = decor(add)
# without(10,20)

# def decor(func):
#     def inner():
#         x = func
#         return x+x
#     return inner
#
# def decor1(func):
#     def inner1():
#         x = func
#         return x+2
#     return inner1
#
# @decor
# @decor1
# def numbers(n):
#     return 10
#
# numbers()

# s = lambda n:n*n
# print(s(5))

# def even(n):
#     # if n%2==0:       #even
#     if n%2!=0:         #odd
#         return n
#     else:
#         return None
# l = [1,2,3,4,5,6]
# s = list(filter(even,l))
# print(s)


# m = lambda n:n+2*n
# print(m(5))

# ASCII values

# s = "python selenium"
# print("The ASCII value of '" + s + "' is", ord(s))


# c = 'python selenium'
# for i in range(len(c)):
#     # print("The ASCII value of '" + c + "' is", c[i],ord(c[i])
#     print("The ASCII Value of Character %c = %d" % (c[i], ord(c[i])))







































