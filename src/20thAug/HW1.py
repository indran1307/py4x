# a,b,c = int(input("Enter the numbers"))
# print(a,b,c)

a=int(input("Enter A:"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))

if a >= b and a >= c:
    print("A is greater than all")
elif b >= c and b >= a:
    print ('B is greater than all')
else:
    print ("C is grater than all")

