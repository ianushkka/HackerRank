import calendar 

days=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

m,d,y=map(int,input().split()) 

c=calendar.weekday(y,m,d) 

print(days[c])