from itertools import combinations_with_replacement 
S,k=input().split() 
k=int(k) 

S=sorted(list(S)) 

seq=list(combinations_with_replacement(S,k)) 

for vals in seq :
    print("".join(vals))
