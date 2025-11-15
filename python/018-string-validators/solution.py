if __name__ == '__main__':
    s = input()
    flag=False
    for i in s :
        if i.isalpha() or i.isdigit() :
            flag=True
            break
            
    print(flag)
    
                
    for i in s :
        if i.isalpha() :
            print("True") 
            break
    else :
        print("False")
        
    
    for i in s :
        if i.isdigit() :
            print("True") 
            break
    else :
        print("False")
            
    for i in s :
        if i.islower() :
            print("True") 
            break
    else :
        print("False")
            
            
    for i in s :
        if i.isupper() :
            print("True") 
            break
    else :
        print("False")
            
            
            
    