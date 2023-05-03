# swapping list


# def swapList(newList):
     
#     newList[0], newList[-1] = newList[-1], newList[0]
 
#     return newList
     
# # Driver code
# newList = [12, 35, 9, 56, 24, 7, 8]
# print(swapList(newList))

#reversing the list
# newList= (input("enter the number :")).split(",")
# # newList = [12, 35, 9, 56, 24, 7, 8]
# print(newList[::-1])

# concanating in the list

# list1=["M","na","i","in"]
# list2=["y","me","s","dra"]
# list1 = (input("enter the first list")).split(",")
# list2 = (input("enter the second list")).split(",")
# result=[]
# for i in range (len(list1)):
#     result.append(list1[i]+list2[i])
# print(result)

# Exercise 3: Turn every item of a list into its square
# numbers= [1,2,3,4,5,6,7]
# result=[]
# for i in range(1,len(numbers)+1):
#     result.append(i*i)
# print(result)

# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i in range(0,len(list1)):
#     print(list1[i], list2[len(list2)-i-1])

# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# index=list1.index(20)
# list1[index]=200
# print(list1)


# dictionary
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dict = dict(zip(keys, values))
# print(dict)


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dict = dict()

# for i in range(len(values)):
#     dict.update({keys[i]: values[i]})
# print(dict)


# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)

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

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# result = dict.fromkeys(employees, defaults)
# print(result)
# print(result["Kelly"])

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# keys = ["name","age","salary","city"]

# res = dict()

# for k in keys:
#     res.update({k: sample_dict[k]})
# print(res)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary"]

# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)


# dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in dict.values():
#     print('200 present in a dict')
    
    
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

# sample_dict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75
# }
# print(min(sample_dict, key=sample_dict.get))


# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }

# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)

# def get_middle_three_chars(str1):
#     print("Original String is", str1)

#     first get middle index number
#     mi = int(len(str1) / 2)

#      use string slicing to get result characters
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)

# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")





