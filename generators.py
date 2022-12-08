# Generators is a special function that helps in generating sequence of values using yield keyword.

# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b
# for x in fib():
#     if x<20:
#         print(x)
#     else:
#         break


# s = lambda n:n+n
# print(s(15))

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# h = list(filter(lambda n:n%2==0,s))
# print(h)

# def decor(func):
#     def inner():
#         x = func
#         return x.upper()
#     return inner
#
# def decor1(func):
#     def inner1():
#         x = func
#         return x.lower()
#     return inner1()
#
# @decor1
# @decor
#
# def strings():
#     return "hello world"
# strings()










