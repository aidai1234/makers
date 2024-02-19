

set1={i for i in range (0,10)if i%2==0} 
set2={i for i in range (0,10)if i%2!=0} 
if set1.intersection(set2): 
    print('Множества пересекаются!') 
else:
    print('Множества не пересекаются!') 
