# ===========Функция=========
# функция -это именновонный блок кода,который может принимать аргументы и возврощать результат 

# def get_sum(x,y): #x,y- это параметры 
#     result=x+y
#     return result 

# print(get_sum(10,20) #10,20- это аргументы 


# 'функции соблюдают принцип DRY (don't repeat yourself)"

# ======Аргументы и параметры========
# параметры- это переменные внутри функции,задаются при создании функции 

# аргументы-это значения,которые мы передаем при вызове функции 

# ===========Виды параметров==========
# 1 Обязательное 
# 2 необязательное 
#    1:с дефолтом (со значением по умолчанию)
#    2: args(все позиционные аргументы)
#    3:kwargs(все лишние именнованые аргументы)

# def func(*args,**kwargs)
# print(*args)
# print(**kwargs)
# print(func(1,2,3,'hi'))


# ===========Виды аргументов=========
# 1 позиционные (по позиции)
# 2 именованные (по названию (параметр= значение))

# def func(a,b,c,d):


# func(1,2,3,4,a=12,12,3,4)


# '---------------------------------------------------''
# num:int=10 
# name:str='makers'

# def sum_(a:int ,b:int):
#     return a+b

# print(sum_(10,3))

# def calc_():
#     try:
#         num1 = float(input('Enter number: ')) 
#         num2 = float(input('Enter number: '))  
#         oper = input('Enter oper: ')  
#         if oper == '+':
#             print(num1+num2)
#         elif oper == '-':
#             print(num1-num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '**':
#             print(num1**num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print('вы ввели не ту операцию')
#     except ValueError:
#         print('введите число, а не символы')
#     except ZeroDivisionError:
#         print('нельзя делить на ноль')



# calc_()

# db = [
#     {'name':'Tima', 'password':hash('123456789')},
#     {'name':'Nick', 'password':hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегестрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно залогинились'

# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '12amsdbmnasdb'))
