class Student:
    University="UET"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(self.name,"Marks: ",sum/3)
s1=Student("Umar",[93,95,98])
s1.get_avg()
s1.name="ironman"
s1.get_avg()