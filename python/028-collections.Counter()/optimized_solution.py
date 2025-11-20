from collections import Counter
X=int(input()) 
sizes=Counter(input().split()) 
N=int(input()) 
balance=0

for i in range(N) :
    size,price=map(int,input().split()) 
    if sizes[str(size)]>0 :
        balance+=price
        sizes[str(size)]-=1 
        
print(balance)