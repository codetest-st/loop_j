'''enter a no. and check it is armstrong or not'''
num=int(input("enter a number:"))
x=0
temp=num
d=0
while num>0:
   d=num%10
   x=x+d**3
   num=num//10
   if temp==x:
      print(f"{temp} is armstrong")
   else:
     print(f"{temp}is not armstrong")  
             
