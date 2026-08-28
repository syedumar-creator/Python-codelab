class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i +",self.img,"j")
    def add(self,num2):                        # __add__  (Dunder Func)
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)
num1=complex(1,3)
num1.show()
num2=complex(2,4)
num2.show()
num3=num1.add(num2)                            # When Dunder num3=num1+num2
num3.show()