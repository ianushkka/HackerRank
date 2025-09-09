X=int(input()) 
size_list=list(map(int,input().split())) 
N=int(input()) 

revenue=0
for i in range(1,N+1) :
    size,price=list(map(int,input().split()))
    
    if size in size_list :
        revenue+=price 
        size_list.remove(size) 
        
        
print(revenue) 
    
        
