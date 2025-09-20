A=set(input().split()) 
n=int(input()) 

flag=False
for i in range(n) :
    
    others=set(input().split()) 
    
    #first check for subset 
    if others.issubset(A) :
        if len(A)>len(others) :
            continue
            
        else :
            break 
            
    else :
        break
        
else :
    flag=True
        
print(flag)