key=int(input("Enter Number: "))
tup=(1,2,3,4,5)
i=0
for el in tup:
    if(el==key):
        print("Found at index ",i)
    i+=1