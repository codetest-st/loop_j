'''print factorial'''
num=int(input("enter a number:"))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    print(f"factorial=",factorial)
    i+=1
