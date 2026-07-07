'''enter a no. and check it is palidrome or not'''
num=int(input("enter a number:"))
x=0
temp=num
while num>0:
   x=x*10+num%10
   num=num//10
   if temp==x:
      print(f"{X} is palidrome")
   else:
     print(f"{x}is not palidrome")          
