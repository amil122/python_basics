
# # a=[1,2,3,4,5]
# # b=map(lambda x : x*2,a)
# # print(list(b)) 



# # number =[23,43,2,53,6,76]  
# # even_number=list(filter(lambda x:x%2==0,number))
# # print(even_number)

# # number =[-23,43,-2,53,-6,76]
# # postive_numbers = list(filter(lambda a:a if a>=0 else None,number))
# # print(postive_numbers)

# # from functools import reduce
# # number =[-23,43,-2,53,-6,76]
# # square = list(map(lambda a:a*a,number))
# # sum = reduce(lambda a,b:a+b,square)
# # print(square)
# # print(sum)


# # list1= [1,2,3,4,5]
# # result = [x*3 if x%2 == 0 else x for x in list1 if x >2]
# # print(result)
# # result1 = list(map(lambda a : a *3 if a%2==0 else a,filter(lambda a : a >2 ,list1)))
# # print(result1)

# # list1 = [43, 6, 39, 53, 3]
# # result = list(filter(lambda a: a if a[-1] = = 0 else a , list1))
# # if result:
# #     print(result[-1])
# # else:
# #     print('nothing')
# # print(result)


# words = ["hello", "world", "python", "lambda", "filter", "functional"]
# long_words = list(filter(lambda word: len(word) > 5, words))
# print(long_words)  # Output: ['python', 'lambda', 'filter', 'functional']


# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# cubed = list(map(lambda x: x**3, numbers))
# print(squared)  # Output: [1, 4, 9, 16, 25]
# print(cubed)  # Output: [1, 8, 27, 64, 125]



sentence = "Functional programming with Python"
vowels = list(filter(lambda ch: ch.lower() in "aeiou", sentence))
print(vowels) 


numbers = list(range(1, 50))
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(divisible) 



sentences = ["hello world", "python programming", "functional lambda"]
hyphenated = list(map(lambda s: s.replace(" ", "-"), sentences))
print(hyphenated)  


words = ["radar", "python", "level", "hello", "madam"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes) 



list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]
product = list(map(lambda x, y: x * y, list1, list2))
print(product) 
