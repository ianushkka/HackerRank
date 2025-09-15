from itertools import groupby 
S=input() 

for key,j in groupby(S) :
    a=(f"({len(list(j))}, {key})") 
    print(a,end=" ")