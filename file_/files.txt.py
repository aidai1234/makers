# ''==============Модули  и пакеты============''
# .py-  c таким расиширением это модуль 
#  package -  несколько модулей 


# ' РАБОТА С ФАЙЛАМИ '
# open()- эта функция открывает файл  в определенном режиме 

# r-read(только для чтения )
# w -write(только для записи,каждый раз файл ощичается )
# a- append(только для записи, добавляется в конец )
# x- создает файл,но если он существует выйдет ошибка 


                        # '=======Read======='
# file = open('test1.txt','r')
# file.close()- обязательно нужно закрывть в конце 
# print(dir(file)) 
# print(file.writable()) #false 
# print(file.readable()) #true 
# print(file.read()) - выйдет вся запись на файле text1.txt
# file.seek(0)
# print(file.read())
# print(file.read(5))
# print(file.readline())- читает по строчно 
# print(file.readlines())


# read-->str , readline-->str, readlines-->list[str]

# print(file.tell())-можем узнать где находится каретка 

# ''==========Write=============''
# file =open('test1.txt','w')
# file.write('makers\nHello World')
# file.writelines(['hello world\n','makers\n'])
# file.close()

# 'write-->str' writelines(-->list[str,str])

# ===============Append===============
# # добавляет записи в конец 
# file=open('test1.txt','a')
# file.write('py33\n')
# file.seek(0)
# file.write('py32')
# file.close()


# =======Контекстный менеджер==========
# with 

# with open('test1.txt') as f:( название переменной)
#     print(f.read())
# print(f.closed) #True - файл закрылся  (проверяет тру или фолс)


