class person:

    def __init__(self):
        self.name = input("Enter the name:")
        self.age = input("Enter the age:")

    def name_of_the_function(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")

person1 = person()
person1.name_of_the_function()

