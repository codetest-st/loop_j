'''---*'''
i=1
while i<=5:
    j=1
    while j<=5-i:
        print("_",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end="")
        if k!=i:
            print("_",end="")
        k=k+1
    print()
    i=i+1
