# output = lambda num : num **2
# print(output(3))
import math

output = lambda num: "even" if num %2 ==0 else "odd"
print(output(10))

op2 = lambda : math.pow(int(input("Enter the number: ")), 2)
print(op2())
