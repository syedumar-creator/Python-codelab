count=0
with open("Sample2.txt","w") as f:
    f.write("1,2,3,4,5,6,7,8")
with open("Sample2.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    for i in nums:
        if(int(i)%2==0):
            count+=1
print(count)