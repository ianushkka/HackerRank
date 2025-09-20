T=int(input()) 

for i in range(T) :

    n=int(input()) 
    A=set(input().split())  
    b=int(input()) 
    B=set(input().split()) 
    
    flag=False
    
    for vals in A :
        
        if vals not in B : 
            break 
            
    else :
        flag=True 
        
    if flag :
        print("True") 
        
    else :
        print("False") 
            
    
    
    
 