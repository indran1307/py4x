class calc:

    def __init__(self):
        print("Testing calc")

    def sum(self, a, b):
        return a+b

    def sub(self,a,b):
        return a-b

problem1 = calc()

sum1 = problem1.sum(10,20)
sub1 = problem1.sub(80,10)

print(sum1, sub1)