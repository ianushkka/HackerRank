from itertools import permutations
S,k=input().split()
k=int(k)
string_lst=list(S)
string_lst.sort()
res_lst=permutations(string_lst,k)

print("\n".join("".join(t) for t in res_lst))