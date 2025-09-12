def average(array):
    
    distinct=set(array) 
    avg=round((sum(distinct))/len(distinct) , 3) 
    
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)