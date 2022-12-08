# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
# for val in fib():
#     if val>30:
#         break
#     print(val)
# fib()

# def countdown(num):
#     while num>0:
#         yield num
#         num = num-1
# val = countdown(10)
# for x in val:
#     print(x)


# def decor(func):
#     def inner():
#         x = func()
#         return x*x
#     return inner
# def decor1(func):
#     def inner1():
#         x = func()
#         return x+x
#     return inner1
# @decor
# @decor1
# def num():
#     return 10
# print(num())

# import xlrd
#
# def excel():
#     path = r"C:\Users\Yashaswini\Desktop\locator_py.xlsx"
#     opening = xlrd.open_workbook(path)
#     access = opening.sheet_by_name("login_page")
#     rows = access.get_rows()
#     # print(rows)
#
#     header = next(rows)
#     # for row in rows:
#     return {row[0].value: (row[1].value,row[2].value) for row in rows}
#         # print(rows[0].value,rows[1].value,rows[2].value, sep=" -- ")
#
# excel()


















