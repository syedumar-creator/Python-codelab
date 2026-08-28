a=int(input("Enter Number: "))
b=int(input("Enter Number2: "))
c=int(input("Enter Number3: "))
if(a>=b and a>=c):
    print("Greatest: ",a)
elif(b>=c):
    print("Greatest: ",b)
else:
    print("Greatest: ",c)