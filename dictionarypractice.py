# # Exercise 1: Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1 = dict()

# for i in range(len(keys)):
#     dict1.update({keys[i]: values[i]})
# print(dict1)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 2: Merge two Python dictionaries into one

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3= {**dict1,**dict2}
# print(dict3)

# # another way

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 3: Print the value of key ‘history’ from the below dict

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 4: Initialize dictionary with default values

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dict1= dict.fromkeys(employees,defaults)
# print(dict1)
# print(dict1[ "Kelly" ])

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 5: Create a dictionary by extracting the keys from a given dictionary

# sampledict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary","city"]

# newdict = {k: sampledict[k] for k in keys}
# print(newdict)

# # another method


# # new dict
# res = dict()

# for k in keys:
#     # add current key with its va;ue from sample_dict
#     res.update({k: sample_dict[k]})
# print(res)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# # Exercise 6: Delete a list of keys from a dictionary

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# # Exercise 7: Check if a value exists in a dictionary

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')  

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 8: Rename key of a dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 9: Get the key of a minimum value from the following dictionary

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# print(min(sample_dict,key=sample_dict.get))


#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# # Exercise 10: Change value of a key in a nested dictionary

# dict1 = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# dict1['emp2']['salary']=8500
# print(dict1)


#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,







