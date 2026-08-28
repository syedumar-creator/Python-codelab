key=int(input("Enter Number: "))
tup=(1,2,3,4,5,6,7)
i=0
while i<len(tup):
    if(tup[i]==key):
        print("Found at index",i)
        break
    else:
        print("Finding...")
        i+=1