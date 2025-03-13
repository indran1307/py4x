class DOG:
    breed = None
    color = None
    name = None
    #age = None
    def __init__(self,name,age):
        print("Automatically called", name, age)
        self.name =name
        self.age =age

    def bark(self):
        print("Dag barks", self.name)

dog1 = DOG('Kiran',12)
dog1.bark()
dog2 = DOG(name = input("Enter the name"), age = int(input("Enter the Age:")))
# dog1.name = 'Kiran'
# print(dog1.name)