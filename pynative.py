# Exercise 1: Print First 10 natural numbers using while loop

# num = 10
# count=1
# while count <=10 :
#     print(count)
#     count = count +1

# Exercise 2: Print the following pattern

# num =5 
# for i in range (1,num+1,1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")



# Exercise 3: Calculate the sum of all numbers from 1 to a given number

# num= int(input("enter the number :"))
# sum=0
# for i in range (1,num+1):
#     sum=sum+i
# print("sum of all number",sum)


# Exercise 4: Write a program to print multiplication table of a given number

# num = int(input("Enter the value"))
# for i in range (1,11):
#     p=num*i
#     print(p)


# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for value in numbers:
#     if value > 500:
#         break
#     elif value > 150:
#         continue
#     elif value %5 ==0:
#         print(value)

# Exercise 6: Count the total number of digits in a number

# count=0
# num=int(input("enter the num :"))
# while(num):
#     num = num//10
#     count=count+1
# print("no. of digits :",count)


# Exercise 7: Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# def print_reverse_num(higher_bound):
#     for num in range(higher_bound,0,-1):
#         print(num , end = ' ')

# input_row = int(input("rows: "))    
# for row in range(input_row,0,-1):
#      print_reverse_num(row)
#      print('')
     
# num =int(input("rows :"))
# for row in range(num,0,-1):
#     for i in range (row,0,-1):
#         print(i,end= " ")
#     print(" ")

# Exercise 8: Print list in reverse order using a loop


# Exercise 9: Display numbers from -10 to -1 using for loop

# num =10
# for row in range(-10,0,1):
#     print(row)
    
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# num =10
# for row in range(-10,0,1):
#     print(row)
# else:
#     print("done")

# Exercise 11: Write a program to display all prime numbers within a range
# Exercise 12: Display Fibonacci series up to 10 terms
# Exercise 13: Find the factorial of a given number

# fact=1
# num=5
# for i in range (num,0,-1):
#     fact=fact*i
# print("factorial :",fact )

# Exercise 14: Reverse a given integer number

# new_number = 0
# input_number = int(input("number :"))
# while(input_number):
#     digit = input_number %10
#     new_number = new_number * 10 + digit
#     input_number = input_number // 10
# print("reverse number :",new_number)
    


# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Exercise 17: Find the sum of the series upto n terms
# Exercise 18: Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")



# column =5
# for i in range(0, column):
#     for j in range(0, i +1):
#         print("*", end=' ')
#     print(" ")

# for i in range(column, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# print this pattern
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *


# rows= int(input("enter the rows"))
# for i in range(1,rows +1):
#     print(' ' * (rows-i),'* ' * i)
    
    
    
    