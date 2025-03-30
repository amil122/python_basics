
# def group_anagrams(words):
#     anagram_dict = {}
#     for word in words :
#         sorted_word = ''.join(sorted(word))
#         print(sorted_word)
#         if sorted_word in anagram_dict:
#             anagram_dict[sorted_word].append(word)
#             print(anagram_dict,'if condition')
#         else :
#             anagram_dict[sorted_word] = [word]
#             print(anagram_dict,'else conditoom')
#     return list(anagram_dict.values())
# a = ['ten', 'ate', 'tea', 'eat', 'net', 'bat']
# b = group_anagrams(a)
# print(b)






# s=' my name is amil'
# new_list = [char for char in s if char in 'aeiou']
# print(new_list)
# lst = ['malayalam','amil']
# for word in lst:
#     if word == word[::-1]:
#         print('it is palindrome')
#     else :
#         print(word ,'not palindrom')




# def factorial(number):
#     if number == 0 :
#         print('give a valid number')
#     elif number == 1:
#         print(number)
#     else:
#         result = 1
#         for i in range(1,number+1):
#             result *= i
#     return result
# print(factorial(5))




# # Example usage:
# input_string = "hello world"
# reversed_string = reverse_string(input_string)
# print("Original:", input_string)
# print("Reversed:", reversed_string)

# lst = [32, 63, 2, 3930, 23]
# max_number = 0
# result = 0
# for i in lst :
#     if i > max_number :
#         max_number = i
# print(max_number)
        
        
        


# lst= [34,23,532,53,943,453]
# max_number = 0
# second_max = 0
# for i in lst :
#     if i > max_number:
#         second_max = max_number
#         max_number = i
#     if i < max_number and i> second_max:
#         second_max = i
# print(second_max)





# nums= [7,52,2,4]
# summ = ''
# nums1 = len(nums)//2
# for i in range(nums1):
#     for j in reversed(range(len(nums)//2)):
#         summ += str(nums[i]) + str(nums[j])
        
# print(summ)




# lst=[32,15,63,22,94]
# j=len(lst)-1
# for i in range(len(lst)//2):
#     lst[i],lst[j]=lst[j],lst[i]
#     j-=1
# print(lst)

# lst = [32, 15, 63, 22, 94]
# i = 0
# j = len(lst)
# while i < j:
#     lst[i], lst[j] = lst[j], lst[i]
#     i += 1
#     j -= 1
# print(lst)

# st = [32, 15, 63, 22, 94]   
# j= len(st)-1
# print(j)




# def my_function(a, b, c):
#     print(a, b, c)

# my_list = [1, 2, 3]
# my_function(*my_list)
# print(*my_list)                               # Equivalent to my_function(1, 2, 3)

# def my_function(*args):
#     print(args)

# my_function(1, 2, 3, 'hello')                 # Output: (1, 2, 3, 'hello')

# mylst= ['amil','jaseel','nothing']
# a,b,c = mylst
# print(a)

# def my_function(*args):
#     print(args)

# my_list = [1, 2, 3]
# my_function(*my_list)                         # Equivalent to my_function(1, 2, 3)




# def smallest_largest(arr):
    
#     smallest = largest = arr[0]

#     for num in arr:
#         if num < smallest:
#             smallest = num
#         elif num > largest:
#             largest = num

#     return smallest, largest
# arr = [45, 12, 67, 3, 92, 18, 35]
# smallest, largest = smallest_largest(arr)
# print(smallest,largest)






# lst1= [23,43,67,96,222,583,786]
# target = 968
# l=0
# u=len(lst1)-1
# while l<=u:
#     mid = (l+u)//2
#     print(lst1[mid])
#     if lst1[mid] == target:
#         print('it is found in the list with the index number of' + str(mid))
#         break
#     if lst1[mid]<target:
#         l = mid+1
#     else:
#         u =mid-1
        
#         break
#     if l==u:
#         print('it is not there')



# dict1= {
#     1:'amil',
#     2:'jaseel',
#     3:'basil'
# }
# max_char = ''
# max_key = None
# for k,v in dict1.items():
#     if max_key is None  or v > max_char:
#         max_char = v
#         max_key = k
# print(max_key)
# print(max_char)





# dict1= {
#     4:'amil',
#     2:'jaseel',
#     3:'basil'
# }
# sorted_dict = sorted(dict1.items(),key= lambda x : x[1])
# new_dict = {k:v for k,v in sorted_dict}
# print(new_dict)




# s= 'my name is muhammed amil'
# dict1= {}
# for i in range(len(s)):
#     count= 0
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             count +=1
#     if s[i] != ' ' :
#         dict1[s[i]]= count

# max_char = ''
# max_key = None
# for k,v in dict1.items():
#     if max_key is None or v > max_char:
#         max_key = k
#         max_char = v
# print(dict1)
# print(max_char)
# print(max_key)




# nums = [4,3,2,7,8,2,3,1]
# res = []
# nums1 =[5,6]
# for i in range(nums):
#     if nums[i] not in res :
#         for j in range(nums1):
#             if nums[i] < nums1[j] :
#                 res.a
                
# s = 'aaabbacbb'
# result = ''
# count = 1
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         result += s[i] + str(count)
#         count = 1
#     else:
#         count += 1
# result += s[-1] + str(count)
# print(result)




# lst1 = [989,43,534,62,13,93]
# n= 534
# i=0
# while i < len(lst1):
#     if lst1[i] == n:
#         print('it is there in the list the index number of '+str(i))
#         break
#     i +=1
# if lst1[i] not in lst1:
#     print('it is not in the list')

# def multiple_occurance(lst1,n):
#     occurance=[]
#     for item in lst1:
#         if item== n:
#             occurance.append(item)
#     return occurance

# lst1 = [989,43,534,43,13,13]
# n = 43
# a=multiple_occurance(lst1,n)
# print(a)







# lst1= [21,42,63,84,94]
# target=42
# l=0
# u=len(lst1)-1
# while l<=u:
#     mid =(l+u)//2
#     if lst1[mid]== target:
#         print('the first position is occured at the index number of '+str(mid))
#         break
#     else:
#         if lst1[mid]< target:
#             l= mid+1
#         else:
#             u = mid-1
            
# if l!=u:
#     print('it is not in the list')



# dict1= {
#     1:'amil',
#     2:'jaseel',
#     3:'basil'
# }

# a = dict1.values()
# b = dict1.keys()
# new_dict = {k:v for k,v in zip(a,b)}
# print(new_dict)

