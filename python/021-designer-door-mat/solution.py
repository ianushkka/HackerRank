N,M=map(int,(input().split()))   #M=3*N

for i in range(1,((N-1)//2)+1) :
    print((".|."*(2*i-1)).center(M,"-"))
    
print("WELCOME".center(M,"-")) 

for i in range((N-1)//2,0,-1) : 
    print((".|."*(2*i-1)).center(M,"-"))
    