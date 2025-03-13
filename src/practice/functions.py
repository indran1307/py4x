# def shar():
#     print("Hello")
# shar()
################################################################
# def get_coordinates():
#     return 10, 20
#
# x, y = get_coordinates()
# print(x, y)

############################################################

# def greet_by_name(name):
#     print("Hello ", name)
#
# name = input("Enter the name\n")
# greet_by_name(name)


# def sum_of_3_numbers(a,b,c):
#     return a+b+c
# result=sum_of_3_numbers(10,20,60)
# print(result)


# def multiple_args(*args):
#     print(args)
#
# multiple_args("indra","reddy","D","s")



my_shopping_list = ['fruits','Grcs','milk']
print(my_shopping_list)
print(len(my_shopping_list))

my_list=[]
def more_items(my_list):
    more_list = input("Enter the item name: ")
    my_list.append(more_list)
    print(my_list)
    return my_list


more_items(my_list)
