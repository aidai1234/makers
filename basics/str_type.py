#                                                           #=========string строки =========
# #строки-неизменяемый тип данных который предназначен для хранения текста заключенного в одинарные или в двойные кавычки
# string1="строками с двойными ковычками "
# string2='строка с одинарными ковычками '
# #string3='не правильная строка"
# string4="don't"-внутри двойной кавычки все одинарные -просто символы 
# string5= """ 
# многострочный текст в тройных кавычках 
# """ #многострочный текст удобно использовать тройные ковычки
# string6='hello'+ 'world'
# print(string6)
# string7='A' *8 #(текст повторится 8 раз также можно поставить слово и оно тоже повторится 8 раз)
# print(string7)
# #================экранизация строк ===================
# #'\n' переносит текст на новую строку 
# print('hello\nworld')
# #hello
# #world
# '\t' #табуляция -  пробел 
# print('hello\tworld')
# #hello    world 
# #'\'=backslash 
# str1='don\'t'#отображает ковычку 
# print(str1)
# str2="don\"t"
# print(str2)
# str3='символ -\\'
# print(str3)



# '\v' #-перенос на новую строку со смещением вправо на длину предыдущей строки 
# print('hello\vworld\vmakers\vbootcamp')- получаетсялестница 
# '\r'#перенос каретки на начало строки  
# print ('makers bootcamp\rHi') каретка- курсор переносится вначало 
# #выйдет Hikers bootcamp
 
#                                                 '==========форматирование строк======='
# #1
# title="iphone14"
# price=150
# format1="мой телефон",title,'стоит' price,'долларов'-это высветиться с ковычками и с запятыми правильно но не красиво будет читаться 
# format2=f'мой телефон {title}'стоит {price}$ -это выйдет одним текстом и читабильно будет 
# print(format2)
# #2
# string='название:'{}цена:{}'
# print(string.format('ipthone14',150))
# #3
# string ="название:%s цена:%s" -обозначает 
# print(string%('iphone',150))

#                                                  #======методы строк======
# #методы-это функции которые относятся к определенному классу к ним можно обращаться через точку 
# dir (str)
# print(dir(str))
# string='makers'
# print(string.upper())#MAKERS аппер переводит все буквы в большие буквы
# print(string.lower())#makers lower- для того чтобы сделать все буквы маленькими 
# print(string.swapcase())#MaKeRs свапкейс делает все наоблорот к примеру -mAkErS
# print(string.title())#hello world --->Hello World меняет заглавные буквы если были маленькие то сделает большими меняет каждое слово 
# print(string.capitalize())#hello world --->Hello world -меняет только  начало первое слово 
# print(string.center(10))#'    hello    ' (10)-это количесвто пробелов / после 10 например можно поставить любой символ например запятая и вместо пробелов будет запятая 
# print(string.count('l'))-показывает количесвто символов (hello)например в хелло есть 2 л поэтому  программа  покажет 2
# string='hello'
# print(string.startswith('a')) - показывает с какой буквы начинается слово (false )-потому что слово начинается с h
# print(string.startswith('h')) - показывает с какой буквы начинается слово (true )-потому что слово начинается с h
# print(string.endswith(o))-показывает последнюю букву тут к примеру True потому что слово заканчивается на о
# string='makers'
# print(string.islower())#makers-->true проверяет является ли все слово маленькми буквами 
# print(string.islower())#makers-->false проверяет является ли все слово маленькми буквами 
# print(string.isupper)#MAKERS->>true проверяет являются ли все слово большими буквами 
# string='1233455'
# print(string.isdigit())- проверяет есть ли в тексте числа здесь к примеру True потому что в слово есть цифры 
# #частичка is -это проверка true/false 
# string'makers'
# print(string.isalpha)-true Проверка на буквы к примеру если в переменной стоят цифры программа выдаст false потому что в переменной нет букв
# string='1123443'
# print(string.isalnum())-проверка и на число и на цифру но не символы   к примеру тут будет true потому что есть цифры 
# string= 'hello world makers bootcamp'
# print(string.split()) - делит слова и буквы  делит на множество частей  то что внутри скобок поставим то и исчезает в тексте
# [::-1]
# len()-вывод длины в  строку  
# #Для замены букв в символьной строке мы можем воспользоваться функцией replace() или методом replace()


#                           "=======INDEKSY==========
# Индекс -порядковый номер элемента в последовательности (символ в строке (индексация начинается с 0)
# 'H E l l O  W O R L D '
#  0 1 2 3 4 5 6 7 8 9 10    
#                 -3 -2 -1

# string='hello world'
# print(string[0])- тут мы обращаемся к букве h
# print(string[7])- тут мы обращаемся к о

# 'срезы'- это под строка (часть строки)
# string='hello world'
# print(string[3:5])-получаем буквы lo 
# string[start:end(не включительно/берем на одну букву больше):step]
# print(string[6:])-возьмет слово только world 
# print(string[:])- выйдет hello world полностью 
# print(string[::-1])-выйдет текст зеркально dlrwo olleh
# print(string[::2])-#hlowrd
# print9string[::3])-#hlwl
# print(string[::4])-#hor
   