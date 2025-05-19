
# Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.



class calculator:

    def __init__(self,x,y,optype):
        self.x=x
        self.y=y
        self.optype=optype

    def calcy(self):
        if self.optype == "add":
            return self.x + self.y
        elif self.optype == "sub":
            return self.x - self.y
        elif self.optype == "mul":
            return self.x * self.y
        elif self.optype == "div":
            return self.x / self.y
        else:
            return "invalid input"

        


a=float(input("enter the first value:"))
b=float(input("enter the second value:"))
op=input("pleace select the operation to be performed : (add,sub,mul,div):")


obj=calculator(a,b,op)

result=obj.calcy()
print(result)