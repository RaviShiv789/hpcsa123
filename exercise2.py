# def function_addition(first_num,second_num) :
#     returned_value = first_num+second_num
#     print("The Addition of the numbers is ",returned_value)
    
# def function_square(first_num,second_num) :
#     returned_value1 = first_num**2
#     print("The Square of the number is ",returned_value1)
    
# def function_exp(first_num,second_num) :
#     returned_value2 = first_num**second_num
#     print("The expo of number is ",returned_value2)
    
def function_calculator() :
    print("1)addition\n 2)square\n 3)expo\n 0)exit")
    choice = int(input("Enter the choice :"))
    
    if (choice == 1):
        first_num = int(input("enter the first number"))
        second_num = int(input("enter the second number :"))
        returned_value = first_num+second_num
        print("The Addition of the numbers is ",returned_value)
        
    elif (choice == 2):
        first_num = int(input("enter the first number"))
        returned_value1 = first_num**2
        print("The square of the numbers is ",returned_value1)
        
        
    elif (choice == 3):
        first_num = int(input("enter the first number"))
        second_num = int(input("enter the second number"))
        returned_value2 = first_num**second_num
        print("The exponenation of number is ",returned_value2)
        
    elif (choice == 0):
        exit
        
    else :
        print("invalid")
choice = "y"
while(choice == 'y'):
    function_calculator()    
    choice = input("\n do you want to continue y : ")    
        
        
        
        
        

