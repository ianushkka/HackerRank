if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        record.append([name,score]) 
        
    names=[n for n,g in record]
    grades=[g for n,g in record]
    
    second_lowest=sorted(set(grades))[1] 
    selected=[n for n,g in record if g==second_lowest]
    selected.sort()
    for ch in selected :
        print(ch) 
    