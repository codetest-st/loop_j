'''______1
___121
__12321....'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print("_",end="")
        j=j+1
    k=1
    while k<=i:
        print(k,end="")
        k+=1
    k=i-1
    while k>=1:
        print(k,end="")
        k-=1
    print()
    i=i+1
