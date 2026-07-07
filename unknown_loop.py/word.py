'''enter a number and print it in word'''
num=int(input("enter anumber:"))
x=0
d=0
while num>0:
    x=x*10+num%10
    num=num//10

while x>0:
    d=x%10
    if d==0:
        print("zero")
    elif d==1:
        print("one")
    elif d==2:
        print("two") 
    elif d==3:
        print("three") 
    elif d==4:
        print("four") 
    elif d==5:
        print("five")
    elif d==6:
        print("six") 
    elif d==7:
        print("seven") 
    elif d==8:
        print("eight") 
    elif d==9:
        print("nine")
    x=x//10
                                     