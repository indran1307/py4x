class person:
    name= None
    age = None
    height = None
    def talk(self):
        print("I can talk")
    def walk(self):
        print("Sleep")

obj1 = person()
print(obj1.name)
obj1.name = "Indra"
print(obj1.name)
obj1.walk()


