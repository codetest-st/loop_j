'''take input of 2nos and print sum every time until user want to exit'''
while True:
    a=int(input("enter a number:"))
    b=int(input("enter a number: "))
    
    print("sum", a+b)

    choice =input("do you want to continue?(yes/no):" )
    if choice =="no" or choice=="NO":
        print("program ended")
        break