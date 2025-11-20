from itertools import product

A=list(map(int,input().split()))
B=list(map(int,input().split()))

lst=list(map(str,product(A,B)))

print(" ".join(lst))