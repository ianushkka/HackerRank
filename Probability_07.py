from math import comb 

N=int(input()) 
alphabet_list=input().split() 

K=int(input()) 
a_count=alphabet_list.count("a") 
no_a_letters=len(alphabet_list)-a_count 

total_combinations=comb(N,K)

if no_a_letters>=K :    

    no_a_combinations=comb(no_a_letters,K) 
    
else :
    no_a_combinations=0
    
probability=1-(no_a_combinations/total_combinations) 


print(round(probability,3))
