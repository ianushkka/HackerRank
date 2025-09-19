n,m=map(int,input().split()) 
arr=list(map(int,input().split()))

A=set(map(int,input().split())) 
B=set(map(int,input().split()))  

score=0

for num in arr :
    if num in A :
        score+=1 
        
    elif num in B :
        score-=1
        
    else :
        continue  
        
print(score)
        
        