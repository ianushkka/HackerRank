from collections import defaultdict 
n,m=map(int,input().split()) 
 
word_collection=defaultdict(list) 

for i in range(1,n+1) :
    word_collection[input()].append(i) 

for j in range(1,m+1) :
    check_word=input() 

    if check_word in word_collection :
        print(*word_collection[check_word]) 

    else :
        print(-1)
