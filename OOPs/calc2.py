class calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self,a,b):
        return a-b
test1 = calc(40,20)

print(test1.sum())
#test1.sub()
