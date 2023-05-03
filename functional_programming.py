
# def function_calculator(received_function):
#     received_function()
    
# def cal_calculation():    
#     choice = int(input("Enter the choice :"))
    
#     if (choice == 1):
#         first_num = int(input("enter the first number"))
#         second_num = int(input("enter the second number :"))
#         returned_value = first_num+second_num
#         print("The Addition of the numbers is ",returned_value)
        
#     elif (choice == 2):
#         first_num = int(input("enter the first number"))
#         returned_value1 = first_num**2
#         print("The square of the numbers is ",returned_value1)
        
        
#     elif (choice == 3):
#         first_num = int(input("enter the first number"))
#         second_num = int(input("enter the second number"))
#         returned_value2 = first_num**second_num
#         print("The exponenation of number is ",returned_value2)
        
#     elif (choice == 0):
#         exit
        
#     else :
#         print("invalid")
# choice = "y"
# while(choice == 'y'):
#     function_calculator(cal_calculation)    
#     choice = input("\n do you want to continue y : ")    
    
# #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    
#     #create my calculator in functional style
    
# from operator import add, sub, mul, truediv
# def calculator():
#     num1= int(input("enter the first number :" ))
#     operator= input("enter the operation :" )
#     num2= int(input("enter the second number :" ))
    
#     operation={
#         "+": add,
#         "-": sub,
#         "*": mul,
#         "/": truediv,
#     }.get(operator)
#     if operation:
#         result=operation(num1,num2)
#         return result
#     else:
#         result="error"
#         return result
    
# print("Result:",calculator())

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# """
# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation
# """

def hof(func,param1,param2= None):
    return func(param1) if param2 is None else func(param1,param2)

#from function_definitions import *
my_addition = lambda first_number,second_number : first_number+second_number
my_square = lambda first_number, second_number = None : first_number**2
my_exponenation = lambda first_number,second_number : first_number**second_number

# def my_calculator():
#     print("****************** MENU ************************")
#     print("1: Addition")
#     print("2: Square")
#     print("3: Exponentation ")
#     choice = int(input ("Please select your choice"))

#     if choice == 1 :
#         first_num = int(input("Please enter First number:"))
#         second_num = int(input("Please enter Second number:"))
#         #returned_value = my_addition(first_num,second_num)
#         returned_value = hof(my_addition,first_num,second_num)
#         print("The Addition of the numbers is ",returned_value)

#     elif choice == 2 :
#         first_num = int(input("Please enter First number:"))
#         #returned_value = my_square(first_num)
#         returned_value = hof(my_square,first_num)
#         print("The Square of the number is ",returned_value)
#     elif choice == 3 :
#         first_num = int(input("Please enter First number:"))
#         second_num = int(input("Please enter Second number:"))
#         #returned_value = my_exponenation(first_num,second_num)
#         returned_value = hof(my_exponenation,first_num,second_num)
#         print("The exponenation of the numbers is ",returned_value)

# def iterative_calculator():
#     while(True):
#         print("Lets start   !!!! ")
#         my_calculator()	
#         choice = input("\n Do you want to continue (Y/N)").lower()     
#         if choice == 'n':
#             break

# iterative_calculator()

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# functional style using function object reference and dictionary to navigate to a function runtime

while(True):
    my_invocation_dict = {1: my_addition , 2 : my_square , 3: my_exponenation}
    print("Lets start   !!!! ")
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    first_num = int(input("Please enter First number:"))
    if choice !=2 :
        second_num = int(input("Please enter Second number:"))

    print('Addition : ' if choice == 1 else 'Square : ' if choice == 2 else 'Exponentation: ' , end = ' ')
    print(my_invocation_dict.get(choice)(first_num,second_num))

    choice = input("\n Do you want to continue (Y/N)").lower()     
    if choice == 'n':
        break

        
    