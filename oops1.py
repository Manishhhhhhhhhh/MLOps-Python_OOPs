class employee:
    
    def __init__(self):
        print("I start getting executed the moment an object is created")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Developer"
        print("Execution Done")

    def travel(self, des):
        print(f"Employee is now travelling to {des}")


sam = employee()

print(sam.salary)
print(sam.id)
sam.travel("Bangalore")