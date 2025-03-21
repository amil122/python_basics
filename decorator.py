
# def mydef(func):
#     def inner():
#         a=func()
#         return a.upper()
#     return inner

# @mydef
# def dec():
#     return "amil"
# print(dec())


# def upper_dec(func):
#     def wrapper(name):
#         a = func(name)
#         return a.upper()
#     return wrapper
    
# @upper_dec
# def name(name):
#     return 'i am amil  '  +  name
# print(name('mammotty'))




# def double_decor(func):
#     def wrapper(m):
#         result = func(m)
#         return [ item *2 for item in result]
#     return wrapper
# @double_decor
# def reverse_list(l):
#     return l[::-1]
# @double_decor
# def upper_list(l):
#     return [item.upper() for item in l]

# print(reverse_list([2,4,3,5,2]))

# print(upper_list(['a','j','m']))

# def decor(func):
#     def inner(m):
#         a = func(m)
#         return a.upper()
# @decor
# def is_upper(name):
#     return 'my name us amil'
# print(is_upper())


# def decorator(func):
#     def wrapper(n):
#         result = func(n)
#         return [item *2 for item in result]
#     return wrapper    

# @decorator
# def lst(l):
#     return  [item.upper() for item in l]
    
# print(lst(['a','f'])) 


# def decorator(func):
#     def wrapper(n):
#         result = func(n)
#         return result.upper()
#     return wrapper
# @decorator
# def upper(name):
#     return 'hello ' + name

# print(upper('amil'))    




