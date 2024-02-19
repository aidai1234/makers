# ====================comprehemsioms==================
# -это генератор с помощью которого,мы можем создавать последовательности,используя цикл for в одну строку 

# елемент for   елемент  in последовательность 
# елемент for   елемент  in последовательность if фильтр 
# елемент if   условие1 else елемент 2  for   елемент  in последовательность 

# compr=[i for in range (6) ]
# print(compr_)

# compr_[]
# for i in range(6):
#     if i%2 ==0:
#     compr_.append(i)
#     else:
#         compr_.append('elem')
# print(compr)
# (0,1,2,3,4,5)-результат 



# list_=[12,None,'hi',123,1,6,2,True]
# new_list_=(i for i in list_ if bool (i)]
# print(new_list)
# #-12,hi,123,1,6,2,true -распечаталось все TRUE 


# ===================Виды comprehensions==========================
# немзменяемые  типпы данных
# str 
# tuple
# boolean 
# frozenset
# None 
# в компетеншен мы можеи использовать только изменяемые данные list ,dict,set

# #comprehention генератор ->()скобки круглые у него 
# compr_==[i for i in range 11]
# print(compr_)
# #0,1,2,3,4,5,6,7,8,9,10,11

# =========Dict comprehension=======
# {1:1,2:4,3:9,4:16}
# dict_={i:i**2 for i in range (1,5)}
# print(dict_)

#=========set_ comprehension========


#=========вложенные comprehension==========
# создайте словарь где ключамами будет число от 1 до 5,а значениями будут списки  с числами от 1 до этого числа

# dict_=()
# for i in range(1,6):
#     key=i 
#     values=[j for j in range (1,i+1)]
#     dict_[key]=values

