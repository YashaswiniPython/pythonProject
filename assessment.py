# # 1.	Write a program to reverse a string without using any inbuilt functions.
#
# string = "hello world" [::-1]
# print(string)
#
# # 3.	Write program to convert upper case to lower case and vice-versa without using inbuilt method.
#
# # string = "PytHOn SElenIUm"
# # m = print(list(string))
# # # print(m)
# # m = string.swapcase()
# # print(m)
# # l = m.swapcase()
# # print(l)
#
# # 4.	Write program to swap two numbers without using 3rd variable.
#
# x = 5
# y = 10
#
# x, y = y, x
# print(x)
# print(y)
#
# # 6.	Create a list of palindromes using list comprehension without using reversed method
#
# names = ["mother", "dad", "listen", "level", "mom"] [::-1]
# print(names)
#
# # 8.	Write a decorator that returns only positive values of subtraction.
#
#
# def decor(func):
#     def sub1(a,b):
#         print("*"*20)
#         print("enter a value:",a)
#         print("enter a value:",b)
#         print("the value of {} and {} is {}".format(a,b,a-b))
#         print("*"*20)
#     return sub1
# @decor
# def sub(a,b):
#     return (a-b)
# sub(20,10)
#
# # 10.	remove duplicates from the list without using inbuilt functions

# 15.	Write a function to print the below output.

# 2.	Write a Program to print ascii values of the characters present in a string.
# c = 'python selenium'
# for i in range(len(c)):
#     # print("The ASCII value of '" + c + "' is", c[i],ord(c[i])
#     print("The ASCII Value of Character %c = %d" % (c[i], ord(c[i])))

# write a program for palindrom
#
# string = input("Enter the string: ")
# if string == string[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not a palindrome")

# fib series
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# val = fib()
# for x in val:
#     if x>20:
#         break
#     else:
#         print(x)

# prime numbers

# num = 20
# If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n / 2
#     for i in range(2, int(num/2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# 1.
# String = "hello world"
# print(String[::-1])

# 2.
# s = "python selenium"
# for i in range (len(s)):
#     print("The ASCII Value of Character %c = %d" % (s[i], ord(s[i])))

# 3.
# string = "PytHOn SElenIUm"
# print(string.swapcase())
# print(string.upper())
# print(string.lower())

# 4. Write program to swap two numbers without using 3rd variable

# x = 10
# y = 11
#
# x,y = y,x
# print(x,y)

# 5.	Write program to read a random line in a file. (ex. 50, 65, 78th line)
import random

# 6. palindrome


# string = input("enter the string")
# if string == string[::-1]:
#     print(string,"entered string is palindrome:")
# else:
#     print("Not an palindrome")
#

# 6.	Create a list of palindromes using list comprehension without using reversed method.
# names = ["mother", "dad", "listen", "level", "mom"]
# def str1():
#     for i in names:
#         if i == i[::-1]:
#             print(i)
        # else:
        #     print("error")
# str1()
# # l1 = list( )

#Write a program to search for a user defined character in the given string and return the corresponding index.
# give the index of s

# s = "hellos"
# print(s[5])

# Write a decorator that returns only positive values of subtraction.

# def decor(func):
# #     def inner(a, b):
# #         print("*" * 30)
# #         print("the value of a", a)
# #         print("the value of b", b)
# #         print("the value of {} and {} is : {}".format(a, b, a - b))
# #         print("*" * 30)
# #         return inner
# #
# # @decor
# # def sub(a,b):
# #     return a-b
# # print(sub(10,20))

# Write a program to get the count of number of instances of a class that is being created.

# class add():
#     def test(self):
#         print("hello")
# i = add()
# i.test()

# 10.	remove duplicates from the list without using inbuilt functions
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# unique = set(items)
# print(list(unique))

# 11.	get the elements that are in list b but not in list a
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# h = list(set(b).difference(set(a)))
# print(h)

# a = ['1', '2', '3']
#
# b = ['1', '2', '3','4']
#
# result_1 = list(set(list_2).difference(list_1))
# print(result_1)

# Write a program to check if the arguments that are passed to a function are more than 5.
# def myFun(*args):
#     for arg in args:
#         print(len(arg))
#
# myFun(a,b,c,d,f,g,t)

# def no_of_argu(*args):
#     # using len() method in args to count
#     return (len(args))
#
#
# print(no_of_argu(2, 5, 4))
# print(no_of_argu(4, 5, 6, 5, 4, 4))
# print(no_of_argu(3, 2, 32, 4, 4, 52, 1))
# print(no_of_argu(1))

# Write a program to convert a string to a list and vice-versa.
# string = "hello world"
# print(list(string))
# list = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# str = ""
# h = str.join(list)
# print(h)

# 18.	Create a dictionary of only repeated characters and their number of occurrences
# in a String using dictionary comprehension.
# s = 'helloworld'
#
# res = {}
#
# for keys in s:
#     res[keys] = res.get(keys, 0) + 1
#
# print ("Count of all characters in GeeksforGeeks is : \n"
#                                              +  str(res))


# def no_of_argu(*args):
#     # using len() method in args to count
#     return (len(args))
# a = 1
# b = 3
# # arguments passed
# n = no_of_argu(1, 2, 4, a)
# # result printed
# print(" The number of arguments are: ", n)

# Write a class named Simple and it should have iteration capability.

# Write a function to print the below output.

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# unique = list(dict.fromkeys(items))
# print(unique)
#
# import os,sys
# data = "hello welcome"
# f = open("practice1.py",'r')
# # f.write(data)
# h = f.read()
# print(h)
# fname = input("enter file name")
# if os.path.isfile(fname):
#     f = open("practice1.py",'r')
# else:
#     print("file doesnt exist")
#     sys.exit(0)
# lcount = wcount = ccount=0
#
# for line in f:
#     lcount = lcount+1
#     ccount = ccount+len(line)
#     words = line.split()
#     wcount= wcount+len(words)
# print("the number of lines",lcount)
# print("the number of characters",ccount)
# print("the number of words",wcount)




# x = bin(10)
# x = oct(223)
# x = hex(20)
# print(x)

# string methods
# a = "helloworld"
# print(a.upper())
# print(a.isupper())
# print(a.lower())
# print(a.islower())
# print(a.capitalize())
# print(a.title())
# print(a.isalpha())
# print(a.isdigit())

# list: it is collection of homogenious and heterogenious datatypes,
# written within sqaure brackets and seperated by comma.

# l = [1,10,4,5,6]
# l1 = [4,5,6,7,8]
# l[1] = 4          #reinitialization
# print(l)
# l.clear()
# del l
# print(l)
# print(l.count(4))   #count of number in list
# m = (l.extend(l1))  #joining number
# print(m)
# l.reverse()      #reverse
# print(l)
# l.sort()
# print(l)


# Tuple: same as list but it wont accept reinitialization. will be within brackets.

# l = (1,2,3,4,5,6,6)
# print(l.count(6))
# print(l.index(3))
# l(2) = 5     reinitialization not possible
# del l


# set : it is collection of homogenious and heterogenious datatypes,
# written within flower brackets and seperated by comma. it wont allow duplicate values.

# add

# s = {1,2,3,4,4,5,6}
# b = {3,4,5,6}
# s.add(10)
# s.remove(4)
# t = s.copy()
# a = s.copy()
# print(s.update(b))

# control statements

# if, elif, else

# biggest of 3 numbers

# a = input("enter first number")
# b = input("enter first number")
# c = input("enter first number")
# if a>b and a>c:
#     print("Biggest number is a",a)
# elif b>c:
#     print("biggest number is b",b)
# else:
#     print("biggest number is c",c)

# iterative statements: while, for

# n = "good morning"
# count = 0
# for i in n:
#     count+= 1
#     print(i)
# print("length is",n,count)

# descending order

# for x in range(20,0,-1):
#     print(x)



# for x in range(10):
#     # if x%2!=0:         #odd
#     if x%2==0:            #even
#         print(x)


# n = "good morning"
# count = 0
# for x in n:
#     count+=1
#     print("the value and index is:",x,"index is",count)

# for i in range(4):
#     for j in range(6):
#         print("the value of {} and {}".format(i,j))

# cart = [10,20,50,70]
# for item in cart:
#     if item>50:
#         print("invalid item")
#     else:
#         print("valid")









