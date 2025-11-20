def minion_game(string):
    stuart=0
    kevin=0
    for i in range(len(string)) :
        if string[i] not in "AEIOU" :
            stuart+=len(string)-i
        else :
            kevin+=len(string)-i  
            
            
    if kevin>stuart :
        print(f"Kevin {kevin}")
        
    elif kevin<stuart :
        print(f"Stuart {stuart}") 
        
    else :
        print("Draw")
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)