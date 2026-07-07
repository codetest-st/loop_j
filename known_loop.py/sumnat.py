'''enter a no. and print sum of natural numbers'''
num=int(input("enter a number:"))
sum=0
i=1
while i<=num:
    sum=sum+i
    print(f"sum=",sum)
    i+=1