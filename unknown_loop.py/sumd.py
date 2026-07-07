'enter a no. and print its digit'''
num=int(input("enter a number:"))
x=0
while num>0:
   x=x+1
   num=num//10
print(f"total digits in number is{x}")          
