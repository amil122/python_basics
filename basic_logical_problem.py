# nums=['aa','abc','abcd','ee']
# count =0
# for i in range(len(nums)):
#     s=str(nums[i])
#     if len(s)%2 == 0:
#         count +=1
# print(count)



# nums = [1,1,2,3,1]
# j = 0
# for i in range(1,len(nums)):
#     if nums[i] != nums[i-1]:
#         nums[j] = nums[i]
#         j += 1
# print(j)


    
# def reverse_string(string):
#     reversed_string = ''
#     for char in string:
#         reversed_string = char + reversed_string
#         print(str(reversed_string))
#     return reversed_string



# def vowels_count(lst):
#     vowel = 'aeiou'
#     vowels = 0
#     constant = 0 
#     for char in lst :
#         if char in vowel:
#             vowels +=1
#         else:
#             constant +=1
#     return vowels,constant

# print(vowels_count('hello'))




# lst1= [43,2,45,64,52,75]
# lst2 = [65,43,64,73]
# result = []
# for i in lst1:
#     for j in lst2:
#         if i in lst2:
#             if i not in result:
#                 result.append(i)
# print(result)



# def compress_string(string):
#     compressed_string = ""
#     count = 1

#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             compressed_string += string[i - 1] + str(count)
#             count = 1

#     compressed_string += string[-1] + str(count)

#     return compressed_string if len(compressed_string) < len(string) else string

# # Example usage:
# input_string = "aabbbccc"
# compressed_string = compress_string(input_string)
# print("Original string:", input_string)
# print("Compressed string:", compressed_string)


# s= 'muhammed amil'
# new_dict = {}
# for i in s :
#     count = 0
#     for j in  s :
#         if i== j:
#             count +=1
#     if i != ' ':
#         new_dict[i] = count
# print(new_dict)

# lst =[34,-2,434,2,-34]
# sum = 0
# for i in lst :
#     if i > 0 :
#         sum += i
# print(sum)






    
# def count_words(sentence):
#     # Split the sentence into words based on whitespace
#     words = sentence.split()
#     print(words)
#     # Return the number of words
#     return len(words)




# input_sentence = "Hello world! This is a sentence."
# word_count = count_words(input_sentence)
# print("Number of words in the sentence:", word_count)



# def fibanocci(lst):
#     result = 1
#     for i in lst:
#         result *= i
#     return result
# input = [1,2,3,4,5]
# print(fibanocci(input))

# dict1= {
#     1:'amil',
#     3:'jaseel',
#     2:'pranav'
    
# }
# sorted_dict = sorted(dict1.items(), key =lambda a:a[0])
# new_dict = {x:y for x,y in sorted_dict}
# print(new_dict)



