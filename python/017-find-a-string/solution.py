def count_substring(string, sub_string):
    start=0
    count=0
    for i in range(0,len(string)-len(sub_string)+1) :
        if string[start:start+len(sub_string)]==sub_string :
            count+=1
        start+=1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)