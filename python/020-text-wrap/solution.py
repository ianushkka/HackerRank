import textwrap

def wrap(string, max_width):
    start=0
    lst=[]
    while len(string)-start> max_width:
        lst.append(string[start:start+max_width])
        start+=max_width
        
    else :
        if len(string)>start :
            lst.append(string[start:])
               
    return "\n".join(lst)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)