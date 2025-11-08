def swap_case(s):
    new=""
    for ch in s :
        if ch.isalpha() :
            if ch.isupper() :
                ch=ch.lower()
            else :
                ch=ch.upper() 
        new+=ch
                
        
            
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)