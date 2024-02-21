# ==================JSON======================
# JavaScript object Notation - Универсальный формат , в котором мы можем хранить данные в типах даных,понятных почти для всех языков программирования

import json 
# json_list= '[1,2,3,4,5]'
# python_list= json.loads(json_list)
# print(python_list)

# дисериализация - перевод с json  строки в python обьекты 
# методы- loads(строка), load(файл) 



# сиреализация - перевод python обьектов в json строку 
методы - dumps(строка),dump(файл)

with open('test.json','r')as file:
    python_data= json.load(file)
print(python_date)


with open('test.json','w') as file:
    jsun.dump(json_data,file)