# =====================встроенные функции===============
# map,filter,reduce,zip,enumerate


# 'ZIP'- это функция которая соединяет несколько последовательностей,(получаем гнератор в котором элементы - tuple) (zip object)

# list_1=[1,2,3,4]
# list_2=['a','b','c']
# list_3=[10.4,10.2,1.3,0.5]

# zipped = zip (list_1,list_2,list_3)
# print(list(zipped))# <zip object at 0x7efklclenl12>
# print(list(zipped))
# print(tuple(zipped))
# print(dict(zipped)) #будет работать только с двумя листами в zip()

# 'ENUMERATE'
# #нумерует последовательность ( по дефолту с 0), (тоже возвращает генератор)
# # <enumerate object 0jlkdwlkxklckwl>

# enumerated = enumerate('hello world ',100)
# print(enumerate)
# print(list(enumerated))
# for elem in emurated:
#     print(elem)

# 'MAP'
# Принимает функцию и последовательность 
# записывает в новую последовательность резудьтат функции  применив ее на каждый элемент последовательности 
# <map object jkkdhkhfhkdf>



# list_=['1','2','4','5']
# mapped=map(int,list_)
# print(list(mapped))


# mapped2=map(str.isdigit,list)
# print(list(mapped2))


# list_=[12,20,30,1,2,4]
# def pow_(x):
#     return x**2 
# map(pow_,list)
# print(list(map(pow_,list_)))



# print(list(map(lambda x: x**2,list_)))


# str_='hello world'
# mapped=(str.upper,str_)
# print(list(mapped))
# print(''.join(list(mapped)))

# 'FILTER'
# возвращает генератор с элементами прошедщими фильтрацию ( какое-то условие)
# фильтр также принимает функцию и последовательность 
# <filter object cdkljcljcjlskdlcsl>

#  list_=[12,-12,1,0,-1]
#  filtered= filter(lambda x: x>0,list_)
#  print(list(filtered))

#  users=[
#     {'name':'makers','age':20},
#     {'name':'anonym','age':15},
#     {'name':'sem','age':25}
# filtered=filter(lambda x: x['age']>18,users)
# print(list(filtered))
#  ]

# 'REDUCE'
# принимает функцию и последовательность и возвращает 1 элемент ( передаваемая функция должна принимать 2 аргумента)
# импортируются из functools 



# from functools import reduce 

# list_=[1,23,45,678,99]
# res= reduce(lambda x,y:x*y ,list_)
# print(res)

# users=[
#     {'name':'makers','age':20},
#     {'name':'anonym','age':15},
#     {'name':'sem','age':25}
# ]
# Res=reduce(lambda x:x['age']<18,users)
# print (res)


# def  func(x,y):
#     if x['age']<y ['age']:
#         return x 
#     else:
#         return y 

# print (reduce(func,users))

Узнать самое меньшее число

# list_=[1,2,4,6,1,9,-1,6,13]
# def func(x,y):
#     if x<y: 
#         return x 
#     else:
#         return y 
# print (reduce(func,list_))



# from functools import reduce 
# res=reduce(lambdax,y: x if x<y else y,list_)
# print(res)