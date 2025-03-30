# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#     	break
#     foods.append(food)
# # Below Approach uses Walrus Operatorfood1 = list()
# while (food := input("What food do you like:= ")) != "quit":
# 	foods.append(food)

# def my_function(*args):
#     print(args)
#     print(type(args))

# my_function(1, 2, 3, 'hello')  # Output: (1, 2, 3, 'hello')

# x = 20  
# y = x  
# x += 1  
# print(y)
# if id(x) == id(y):  
#     print("x and y do not refer to  the same object")  
# import copy
# list1= [1,2,3,4]
# list2= copy.copy(list1)

# list2.append(5)
# print(list1)  
# print(list2)