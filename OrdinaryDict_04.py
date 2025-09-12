from collections import OrderedDict 

N=int(input()) 

dictionary=OrderedDict() 

for i in range(N) :
    entered_line_list=input().split() 
    price=int(entered_line_list[-1]) 
    
    name=" ".join(entered_line_list[ :-1])

    if name in dictionary :

        dictionary[name]+=price

    else :
        dictionary[name]=price  


for k,v in dictionary.items() : 

    print(k,v) 
