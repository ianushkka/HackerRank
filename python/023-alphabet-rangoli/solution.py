import string
s=string.ascii_lowercase

def print_rangoli(size):
    
    alphabets=list(s[:size])  #abc
    alphabets.reverse() #cba

    lst=[]
    for i in range(1,size) :
        left=list(alphabets[:i]) #cba
    
        if len(left)>1 :
            right=left[-2: :-1]
            left.extend(right)
    
        print(("-".join(left)).center((4*size)-3,"-"))
        lst.append(("-".join(left)).center((4*size)-3,"-"))

    #middle line
    left=alphabets
    right=left[-2: :-1]
    left.extend(right) 
    print("-".join(left))

    #print("-".join(alphabets))

    #below mirror
    for i in range(-1,-size,-1) :
        print(lst[i])
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)