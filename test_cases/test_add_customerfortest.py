class Add_Customer_For_Testing:
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name


obj = Add_Customer_For_Testing("suhas")
print(obj.show())
