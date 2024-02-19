#                   '============циклы================'
# циклы -это блок кода который отрабатывает несколько раз 
# 1-  for -жто цикл который работает итеррируемым обьектом цикл заканчивает свою работу когда он доходит до последнего элемента иттерирукемого обьекта 

# 'Итерируемый обьект -это какая-то последовательность которую мы можем перебрать  Например list [1,2,3],'hello world', {'a':} (1,2,3,4)(tuple)
# list 
# str
# dict
# tuple - это все иттерируемые то есть то что мы можеим разобрать по одному 
# Итерация - процесс перебора иттеруемого
# #2. while -цикл который работает до тех пор пока условие верное

# 'WHILE'

# count=0 
# while count<10:#TRUE 
#     print(count)
#     count=count+1


# ===========ключевые слова в циклах=====================
#break - оператор который останавлтивает работу цикла (ломает)
#continue- оператор который пропускает итерацию(продолжает с другой итерации)

# for i in range(start,end,step)
# генератор последовательности от start до end 
# print(list(range(1,11)))-не включительно 
# можно добавть шаг  (list(range(1,11,2))-последовательность повторится через кажде 2 

# # for i in range(0,21):
# #     print(i)
# # if i==10:
# #     continue 
# # print(i)


# # for i in ['1','2','3','4','5','hello world'] :
# # if i.isdigiy():
# #     print(int(i)#-'1'-->1, '2'--->2
# # elif i.isalpha():
# #     print('я не могу перевести буквы в число ')
# #     break 
# # else:
# #     print('все прошло хорошо !')


# count=0
# password=input('Введите пароль ')
# while True:
#     print(count)
#     if str(count))==password
#     PRINT('Вот ваш пароль: ', password)
#     break


#     count=count+1 #count +=1  можно написать так 

# while True:
#     if count ==0:
#         continue
#     if count == 1:
#         break 
#     print(count)
#     count+=1

    #else- в цикле работает тогда когда условие цикла становится false ,если же сработал break то  else не работает 



'==============================Метода set========================'
# print(dir(set()))
'----------------------'
# pop - удаляет случайный элемент из set 
# set2 = {1,2,3}
# popped = set2.pop()
# print(popped)
# print(set2)
'----------------------'
# add - добавляет элемент в set
# set3 = {1,2,3}
# set3.add(3) 
# print(set3) # {1, 2, 3}
'----------------------'
# remove - удаляет элемент из set по значению
# set4 = {1,2,3}
# set4.remove(3)
# print(set4)
'----------------------'
# difference (-)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 - set2) # {1,2}
# print(set2 - set1) # {4,5}
# print(set1.difference(set2)) # {1, 2}
# print(set2.difference(set1)) # {4, 5}

# set3 = {5, 6, 7}
# set4 = {6, 8, 9}
# print(set3 - set4) # {5, 7}
# print(set4 - set3) # {8, 9}
'----------------------'
# symmetric_difference
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}
# print(set1)
'----------------------'
# intersection (&)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1.intersection(set2)) # {3, 4}
# print(set1 & set2) # {3, 4}

'----------------------'
# union - обьеденяет сеты
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# print(set1.union(set2))
'----------------------'
# update 
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# set1.update(set2)
# print(set1) # {1, 2, 3, 4, 5, 6, 7}