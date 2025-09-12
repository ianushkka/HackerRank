from collections import namedtuple 
N=int(input()) 

order_list=input().split() 

Student=namedtuple('Student',order_list)

total_marks=0

for i in range(N) :
    data=input().split() 
    student=Student(*data)  #To create fields inside instance , it is necessary to unpack otherwise data is list containing strings 

    total_marks+=int(student.MARKS) 

avg=round(total_marks/N,2) 

print(avg)



