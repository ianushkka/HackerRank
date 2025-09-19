from collections import defaultdict

K=int(input()) 

room_list=list(map(int,input().split()))

room_count=defaultdict(int)


for room in room_list :
    room_count[room]+=1 
    
rooms=list(room_count)
    
vals=list(room_count.values())

index=vals.index(1) 

print(rooms[index])
 

