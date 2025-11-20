def merge_the_tools(string, k):
    start=0
    for i in range(len(string)//k) :
        sub=string[start:start+k] 
        unique=""
        start+=k
        for j in sub :
            if j not in unique :
                unique+=j
        print(unique)
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)