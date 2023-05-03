# # for reversing the list
# list1=[100,200,300,400,500]
# list1.reverse()

# # re reversing the list
# list1= list1[::-1]
# print(list1)    

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 2: Concatenate two lists index-wise

# list1= ["m","na","i","vik"]
# list2= ["y","me","s","as"]

# result=[]
# for i in range (len(list1)):
#     result.append(list1[i]+list2[i])
# print(result)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 3: Turn every item of a list into its square

# numbers = [1, 2, 3, 4, 5, 6, 7]
# square=[]
# for i in range(1,len(numbers)+1):
#    square.append(i*i)
# print(square)

# # another method

# numbers = [1, 2, 3, 4, 5, 6, 7]
# for i in (numbers):
#     square=i*i
#     print(square)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# Exercise 4: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# list3=[i+j for i in list1 for j in list2]       
# print(list3)
# # another method

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3=[]
# for i in list1:
#     for j in list2:
#         list3=i+j
#         print(list3)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 5: Iterate both lists simultaneously

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i, j in zip(list1, list2[::-1]):
#     print(i, j)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 6: Remove empty strings from the list of strings

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2=[]
        
# list2 = list(filter(None, list1))
# print(list2)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# # Exercise 7: Add new item to list after a specified item

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# Exercise 8: Extend nested list by adding the sublist

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)
# print(list1)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

      
# #Exercise 9: Replace list’s item with new value if found

# list1 = [5, 10, 15, 20, 25, 50, 20]

# index=list1.index(15)
# list1[index]=200
# print(list1)

# # Exercise 10: Remove all occurrences of a specific item from a list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)
    
  