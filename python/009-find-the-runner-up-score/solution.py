if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximum=max(arr)
    count=arr.count(maximum) 
    
    for i in range(count) :
        arr.remove(maximum) 
        
    new_max=max(arr) 
    print(new_max)
    