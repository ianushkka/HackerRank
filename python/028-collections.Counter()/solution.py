X=int(input()) 
sizes=list(map(int,input().split())) 
N=int(input()) 
balance=0

for i in range(N) :
    size,price=map(int,input().split()) 
    if size in sizes :
        balance+=price
        sizes.remove(size) 
        
print(balance)


