if __name__ == '__main__':
    N = int(input())
    lst=[]
    
    for i in range(N) :
        entered=input().split()
        
        if entered[0]=="append" :
            lst.append(int(entered[1]))
            
        elif entered[0]=="insert" :
            lst.insert(int(entered[1]),int(entered[2]))
            
        elif entered[0]=="remove" :
            lst.remove(int(entered[1]))
            
        elif entered[0]=="sort" :
            lst.sort()
            
        elif entered[0]=="pop" :
            lst.pop()
            
        elif entered[0]=="reverse" :
            lst.reverse()
            
        else :
            print(lst)
            