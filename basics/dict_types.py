#==========СЛОВАРИ===============
#dict-это изменяемый итерируемый неупорядоченный неидексируемый тип данных для хранени данных в парах (ключ:заключение)

# user= {'name':"sultan", 'age':20,'nick':'katana'}
# print(user['age'])#20
# print(user['nick'])#katana
# print(user['name'])#sultan 

# user={'a':123, "b":20, "c":20}-значения могут повторяться но ключт нет
# #{ключ:значения ,ключ:значение...}
# #ключ- не изменяемый тип данных уникальный (если ключ повторяется то сохранится тот который является последним )
# значение- любые: и изменяемые и не изменяемые тип данных/Могут повторяться 


#========================СОЗДАНИЕ========================
# dict1={'a':1,'b':2}
# dict2=dict([('a',1),('b',2)])
# dict3=dict(['a1','b2'])
# print(dict3)
# dict4={}
# dict4['name']='tima'
# dict4['age']=100
# dict4['nick']='collection'
# print(dict4)


# '==========================МЕТОДЫ СЛОВАРЕЙ====================='
# #get-метод который возвращает значение по ключу если такого ключа нет то возвращает  дефолтное значение чаще всего None
# user={

#     'name':'Nick',
#     'age':100,
#     'number':'+1234566'
# }
# print(user['name'])#nick 
# print(user.get('name ')) #Nick
# print(user.get('id'))#none #потому что есть метод get,огда обращаемся без него будет ошибка  error

# #pop-удаляет пару по ключу и возвращает значение 
# dict_= {'a' :1, 'b':2,'c':g'}
# popped_values=dict_.pop(a)
# print(popped_values)#удалиться ключ 'a',значение 1 останется

#popitem -удаляет последнюю пару и возвращает ее 
# dict_{'a':1,'b':2,'c':3}
# popped_values=dict_.popitem()
# print(popped_values)#('c',3)

#print (dir(dict()))


#update-расширяет словарь парами из второго словаря 
# dict1={1:'a',2:'b'}
# dict2={3:'c',4:'d'}
# dict1.update(dict2)
# print(dict1)

# #clear -очищает словарь 
# dict_={1:1,2:2,3:3}
# dict_.clear()
# print(dict_) #{}-очистился 

#fromkeys- метод для создания нового словаря  использую список ключей 
# dict_=dict.fromkeys([1,2],True)
# print(dict_)#{1:None,2:None}

# dict2=dict.fromkeys('abcd',0)
# print(dict2)#{'a':0,'b':0,'c':0,'d'=0}

#items -метод который достает ([ключ,значение]),([ключ,значение])
 #keys-метод который возвращает ключ 
 #values-метод который возвращает значения
 #  

# dict_={'a':1,'b':2,'c':3}
# print(dict_.values())
# print(dict_.keys())
# print(dict_.items())

# '==============ЦИКЛЫ с dict==================='
# dict_={'a':1, 'b':2,'c':3}
# print(dict_['a'])
# print(dict_['b'])
# for i in dict_:
#     print(i)

