with open("Sample.txt","w") as f:
    f.write("Hey There\nIt's Python")
with open("Sample.txt","r") as f:
    data=f.read()
    print(data)
    new_data=data.replace("Python","java")
    print(new_data)