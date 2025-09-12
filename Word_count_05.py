from collections import OrderedDict 

n=int(input()) 
d=OrderedDict()

for i in range(n) :
    data=input() 
    
    if data in d :
        d[data]+=1 
        
    else :
        d[data]=1 
        
count=0 
for i in d :
    count+=1 
    
print(count) 

for i in d :
    print(d[i] , end=" ")
    