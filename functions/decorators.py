# '=======Функция высшего порядка============'
# функция высшего порядка это функция которая принимает в аргументы другую функцую,создает внутри себя другую функцию,вызывает функцию и возвращает функцию 
# def func1():
#     return 'hi'

# def func2(func):
#     print(func_())

# func2(func1)


# ''================= декораторы=============''
# Декораторы-это функции высшего порядка,которая нужна для расширения функционала другой фцнкции не изменяя ее (функция оберток )
# def decorator_glushitel(func):
#     def wrapper(*args,**kwargs):
#         text=func(*args,**kwargs)
#         res='тихо '+text 
#         print(res)
#     return wrapper
# def gun():
#     return ('стрелять')

# decorator_glushitel(gun)
# wrapper() #способ использовать декоратор в ручную 
# =========================================================================
# def decorator_glushitel(func):
#     def wrapper(*args,**kwargs):
#         text=func(*args,**kwargs)
#         res='тихо '+text 
#         print(res)
#     return wrapper
# @decorator_glushitel
# def gun():
#     return ('стрелять')
# gun()# способ использовать декоратор при помощи синтаксического сахара

# '-----------------------------------------------------------------------'
# from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print('start:',datetime.now())
#         func()
#         print ('finish',datetime.now())
#     return  wrapper 
# def hello():
#     print('hello world')

# wrapper=decorator(hello)
# wrapper()


# --------------------------------------------------------------------------------------------------
# def func_start_time(func):

# def wrapper(*args,**kwargs):
#     print('start:',datetime.now())
#     func(*args,**kwargs)
#     return wrapper 
# @func_start_time
# def sum_(a,b):
#     print(a+b)


# sum_(20,10)
# -------------------------------------------------------------------------------------------------------
# def decorator(num):
#     def inner_decorator (func):
#         def wrapper(*args,**kwargs)
#         for i in range(num):
#             func(*args,**kwargs)
#         return wrapper 
#     return inner_decorator
# @decorator(10)
# def hello():
#     print('hello world')
# hello()


# 1Напишите декоратор call_function, который печатает перед вызовом полученной функции строку:
#  Вызываю функцию <имя_функции>
# Затем следует вызов функции. После вызова функции должна печататься строка:
#  "Вызов функции <имя_функции> прошёл успешно"
# Ввод:
# Python

# @call_functiondef first():
#     print("hello world")
#     return "hello world"
# first()
# Вывод:
# Вызываю функцию first
# hello world 
# Вызов функции first прошёл успешно


# def call_function(func):
#     def wrapper(*args,**kwargs):
#         print('Вызываю функцию',func.__name__())
#         func(*args,**kwargs)
#         print('Вызов функции',func.__name__,'прошел успешно')
#         return wrapper 


# dSPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [i[0] for i in SPL_Patrons if i[1] > 100] 
# print(readers)