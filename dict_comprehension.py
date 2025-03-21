
# mydict ={'name' :['Muhammed Amil','nazal'],'age':22,'place':'Kannur'}
# mydict['email']='amil@gmai.com'
# if 'name' in mydict:
#     print(mydict['name'])
# mydict_copy = mydict.copy()
# print(mydict_copy)
# mydict_copy['job']='dev'
# print(mydict_copy)


# def add(x,y):
#     c = x+y
#     return c
# add(2,3)

# def greeting():
#     c='hello'
#     d='world'
#     return c,d
# result = greeting()
# print(result)
    
# def add(*a):
#     b= 0
#     for i in a:
#         b = b+i
#     print(b)    
    
# add(23,34,232,33)

# dicts = { i:(i**3 if i%2==True else i==False) for i in range(1,9) }
# print(dicts)

# ages =[22,32,43,432,75,33]
# dicts = {age:('YOUNG' if age<=100 else 'false')for age in ages}
# print(dicts)

# old_price= {
#     'compound effect':11,
#     'atomic habbits':9,
#     'twelve pillers':3,
    
# }
# dollar_to_pound=0.93
# dicts={k:v*dollar_to_pound for k,v in old_price.items() if v<=10}
# print(dicts)


# list_of_dicts = [
#     {'name': 'John', 'age': 25, 'city': 'New York'},
#     {'name': 'Alice', 'age': 30, 'city': 'San Francisco'},
#     {'name': 'Bob', 'age': 22, 'city': 'Chicago'}
# ]
# key_to_exclude = 'age'
# new_list_of_dicts = [{k: v for k, v in a.items() if k != key_to_exclude} for a in list_of_dicts]

# print(new_list_of_dicts)


# dicts={
#     1:'abc',
#     2:'amal',
#     3: 'jaseel'
# }
# a = dicts.values()
# b = dicts.keys()
# new_dict = {i:v for i,v in zip(a,b)}
# print(new_dict)



# dicts ={}
# s= 'my name is amil'
# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count +=1
#     dicts[s[i]]= count
# print(dicts)
 

# s= 'my name is amil'
# b ={x:s.count(x) for x in s if x!= ' '}  
# # print(b)

# dicts={
#     'mbcdef':434344,
#     'amal':334,
#     'jaseel':3223
# }
# val = sorted(dicts.items(), key= lambda x:x[0])
# print(val)
# val1 = {x:y for x,y in val}
# print(val1)